# Draft: a futuristic book on a ship's console, a planet outside the window. Cycles, CPU.
import bpy, math, sys, os, random
from mathutils import Vector
A = dict(a.split('=') for a in sys.argv[1:] if '=' in a)
OUT = A.get('out', 'draft.png'); VIEW = A.get('view', 'phone'); SAMPLES = int(A.get('samples', 64)); SCALE = int(A.get('scale', 100)); MODE = A.get('mode', 'still'); PULSE = float(A.get('pulse', 1.0)); ANIM = A.get('anim', 'frames'); FPS = 20; F = 50
HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icon')  # tex_icon.py writes the cover here; ICON = int(A.get('icon', 1))
bpy.ops.wm.read_factory_settings(use_empty=True)
S = bpy.context.scene
S.render.engine = 'CYCLES'; S.cycles.device = 'CPU'; S.cycles.samples = SAMPLES
S.cycles.use_denoising = True; S.cycles.use_adaptive_sampling = True; S.cycles.adaptive_threshold = 0.03
S.cycles.max_bounces = 8; S.cycles.caustics_reflective = False; S.cycles.caustics_refractive = False
S.render.threads_mode = 'AUTO'
if VIEW == 'icon': S.render.resolution_x, S.render.resolution_y = 1024, 1024
elif VIEW == 'phone': S.render.resolution_x, S.render.resolution_y = 780, 1690
else: S.render.resolution_x, S.render.resolution_y = 1920, 1200
S.render.resolution_percentage = SCALE
try:
    S.view_settings.view_transform = 'AgX'; S.view_settings.look = 'AgX - Medium High Contrast'
except Exception as e: print('view', e)

def mat(name):
    m = bpy.data.materials.new(name); m.use_nodes = True
    nt = m.node_tree; b = nt.nodes.get('Principled BSDF'); return m, nt, b
def setp(b, **k):
    for key, v in k.items():
        b.inputs[key.replace('_', ' ')].default_value = v
def obj_mat(o, m): o.data.materials.clear(); o.data.materials.append(m)
def cube(name, size, loc, m=None, bevel=0.0, parent=None):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc); o = bpy.context.object; o.name = name
    o.scale = size; bpy.ops.object.transform_apply(scale=True)
    if bevel:
        md = o.modifiers.new('bev', 'BEVEL'); md.width = bevel; md.segments = 4
    bpy.ops.object.shade_smooth()
    if m: obj_mat(o, m)
    if parent: o.parent = parent
    return o
def emit(name, color, strength):
    m, nt, b = mat(name); setp(b, Base_Color=(0, 0, 0, 1), Emission_Color=(*color, 1), Emission_Strength=strength * PULSE, Roughness=0.5); return m
CY = (0.22, 0.78, 1.0); GOLD = (1.0, 0.72, 0.36); AMBER = (1.0, 0.42, 0.1)

# ---------- world: stars ----------
W = bpy.data.worlds.new('w'); S.world = W; W.use_nodes = True; nt = W.node_tree
bg = nt.nodes['Background']
vor = nt.nodes.new('ShaderNodeTexVoronoi'); vor.inputs['Scale'].default_value = 190; vor.feature = 'F1'
ramp = nt.nodes.new('ShaderNodeValToRGB'); ramp.color_ramp.elements[0].position = 0.0; ramp.color_ramp.elements[0].color = (1, 1, 1, 1)
ramp.color_ramp.elements[1].position = 0.07; ramp.color_ramp.elements[1].color = (0, 0, 0, 1)
noi = nt.nodes.new('ShaderNodeTexNoise'); noi.inputs['Scale'].default_value = 1.6; noi.inputs['Detail'].default_value = 6
neb = nt.nodes.new('ShaderNodeValToRGB'); e = neb.color_ramp.elements
e[0].position = 0.42; e[0].color = (0.0, 0.0, 0.004, 1); e[1].position = 0.9; e[1].color = (0.006, 0.003, 0.018, 1)
mul = nt.nodes.new('ShaderNodeMixRGB'); mul.blend_type = 'MULTIPLY'; mul.inputs[0].default_value = 1
add = nt.nodes.new('ShaderNodeMixRGB'); add.blend_type = 'ADD'; add.inputs[0].default_value = 1
bright = nt.nodes.new('ShaderNodeTexNoise'); bright.inputs['Scale'].default_value = 90
nt.links.new(vor.outputs['Distance'], ramp.inputs[0]); nt.links.new(ramp.outputs[0], mul.inputs[1]); nt.links.new(bright.outputs[0], mul.inputs[2])
nt.links.new(noi.outputs[0], neb.inputs[0]); nt.links.new(mul.outputs[0], add.inputs[1]); nt.links.new(neb.outputs[0], add.inputs[2])
nt.links.new(add.outputs[0], bg.inputs['Color']); bg.inputs['Strength'].default_value = 12.0

# ---------- console (the desk) ----------
m_desk, nt, b = mat('desk'); setp(b, Base_Color=(0.012, 0.016, 0.03, 1), Metallic=0.9, Roughness=0.22, Coat_Weight=0.4, Coat_Roughness=0.05)
n = nt.nodes.new('ShaderNodeTexNoise'); n.inputs['Scale'].default_value = 3; n.inputs['Detail'].default_value = 8
mp = nt.nodes.new('ShaderNodeMapping'); mp.inputs['Scale'].default_value = (1, 160, 1); tc = nt.nodes.new('ShaderNodeTexCoord')
r = nt.nodes.new('ShaderNodeMapRange'); r.inputs['To Min'].default_value = 0.16; r.inputs['To Max'].default_value = 0.34
nt.links.new(tc.outputs['Object'], mp.inputs[0]); nt.links.new(mp.outputs[0], n.inputs['Vector']); nt.links.new(n.outputs[0], r.inputs[0]); nt.links.new(r.outputs[0], b.inputs['Roughness'])
cube('desk', (2.6, 1.3, 0.06), (0, 0.10, -0.03), m_desk, bevel=0.006)
# glowing dock ring the book rests on, plus inlaid lines running to the back
m_cy = emit('cy', CY, 3.2); m_cy_soft = emit('cys', CY, 0.9); m_gold_e = emit('golde', GOLD, 5)
bpy.ops.mesh.primitive_torus_add(major_radius=0.215, minor_radius=0.0011, major_segments=128, location=(0, 0, 0.0006)); obj_mat(bpy.context.object, m_cy)
bpy.ops.mesh.primitive_torus_add(major_radius=0.245, minor_radius=0.0007, major_segments=128, location=(0, 0, 0.0004)); obj_mat(bpy.context.object, m_cy_soft)
for x in (-0.42, -0.30, 0.30, 0.42):
    cube('inlay', (0.0022, 0.9, 0.001), (x, 0.28, 0.0003), m_cy_soft)
for i in range(18):  # tick marks round the dock: one per book
    a = i / 18 * 2 * math.pi; rr = 0.268
    o = cube('tick', (0.012, 0.002, 0.001), (rr * math.cos(a), rr * math.sin(a), 0.0004), m_gold_e); o.rotation_euler.z = a

# ---------- the book ----------
book = bpy.data.objects.new('book', None); S.collection.objects.link(book)
BW, BH, BT = 0.165, 0.238, 0.032
m_cov, nt, b = mat('cover')
tb = nt.nodes.new('ShaderNodeTexImage'); tb.image = bpy.data.images.load(os.path.join(HERE, 'cover_base.png'))
tg = nt.nodes.new('ShaderNodeTexImage'); tg.image = bpy.data.images.load(os.path.join(HERE, 'cover_gold.png')); tg.image.colorspace_settings.name = 'Non-Color'
tl = nt.nodes.new('ShaderNodeTexImage'); tl.image = bpy.data.images.load(os.path.join(HERE, 'cover_glow.png')); tl.image.colorspace_settings.name = 'Non-Color'
mixc = nt.nodes.new('ShaderNodeMixRGB'); mixc.inputs[2].default_value = (1.0, 0.78, 0.42, 1)
nt.links.new(tg.outputs[0], mixc.inputs[0]); nt.links.new(tb.outputs[0], mixc.inputs[1]); nt.links.new(mixc.outputs[0], b.inputs['Base Color'])
rr = nt.nodes.new('ShaderNodeMapRange'); rr.inputs['To Min'].default_value = 0.42; rr.inputs['To Max'].default_value = 0.2
nt.links.new(tg.outputs[0], rr.inputs[0]); nt.links.new(rr.outputs[0], b.inputs['Roughness'])
mr = nt.nodes.new('ShaderNodeMapRange'); mr.inputs['To Min'].default_value = 0.55; mr.inputs['To Max'].default_value = 1.0
nt.links.new(tg.outputs[0], mr.inputs[0]); nt.links.new(mr.outputs[0], b.inputs['Metallic'])
b.inputs['Emission Color'].default_value = (*CY, 1)
em = nt.nodes.new('ShaderNodeMath'); em.operation = 'MULTIPLY'; em.inputs[1].default_value = 2.2 * PULSE
nt.links.new(tl.outputs[0], em.inputs[0])
emc = nt.nodes.new('ShaderNodeMixRGB'); emc.inputs[1].default_value = (*CY, 1); emc.inputs[2].default_value = (1.0, 0.7, 0.32, 1); nt.links.new(tg.outputs[0], emc.inputs[0]); nt.links.new(emc.outputs[0], b.inputs['Emission Color'])
emg = nt.nodes.new('ShaderNodeMath'); emg.operation = 'MULTIPLY_ADD'; emg.inputs[1].default_value = 0.9; nt.links.new(tg.outputs[0], emg.inputs[0]); nt.links.new(em.outputs[0], emg.inputs[2]); nt.links.new(emg.outputs[0], b.inputs['Emission Strength'])
bump = nt.nodes.new('ShaderNodeBump'); bump.inputs['Strength'].default_value = 0.35; bump.inputs['Distance'].default_value = 0.0006
fine = nt.nodes.new('ShaderNodeTexNoise'); fine.inputs['Scale'].default_value = 900
addh = nt.nodes.new('ShaderNodeMath'); addh.operation = 'MULTIPLY_ADD'; addh.inputs[1].default_value = 0.06
nt.links.new(fine.outputs[0], addh.inputs[0]); nt.links.new(tg.outputs[0], addh.inputs[2]); nt.links.new(addh.outputs[0], bump.inputs['Height']); nt.links.new(bump.outputs[0], b.inputs['Normal'])
setp(b, Coat_Weight=0.25, Coat_Roughness=0.12)
m_shell, nt, b = mat('shell'); setp(b, Base_Color=(0.02, 0.03, 0.07, 1), Metallic=0.75, Roughness=0.36, Coat_Weight=0.2)
m_page, nt, b = mat('pages'); setp(b, Base_Color=(0.78, 0.72, 0.6, 1), Roughness=0.8)
wv = nt.nodes.new('ShaderNodeTexWave'); wv.inputs['Scale'].default_value = 420; wv.bands_direction = 'Z'
tc = nt.nodes.new('ShaderNodeTexCoord'); nt.links.new(tc.outputs['Object'], wv.inputs['Vector'])
bp = nt.nodes.new('ShaderNodeBump'); bp.inputs['Strength'].default_value = 0.6; nt.links.new(wv.outputs[0], bp.inputs['Height']); nt.links.new(bp.outputs[0], b.inputs['Normal'])
cube('back', (BW, BH, 0.004), (0, 0, 0.002), m_shell, bevel=0.0012, parent=book)
cube('pages', (BW - 0.012, BH - 0.012, BT - 0.009), (0.002, 0, 0.004 + (BT - 0.009) / 2), m_page, bevel=0.0006, parent=book)
cube('seam', (BW - 0.006, BH - 0.006, 0.0012), (0.001, 0, BT - 0.0062), emit('seam', CY, 4.5), parent=book)
hinge = bpy.data.objects.new('hinge', None); S.collection.objects.link(hinge); hinge.parent = book; hinge.location = (-BW / 2 + 0.003, 0, BT - 0.004)
HX, HZ = -BW / 2 + 0.003, BT - 0.004
m_pg1, nt, b = mat('page1'); tp = nt.nodes.new('ShaderNodeTexImage'); tp.image = bpy.data.images.load(os.path.join(HERE, 'page.png')); nt.links.new(tp.outputs[0], b.inputs['Base Color']); setp(b, Roughness=0.75)
bpy.ops.mesh.primitive_plane_add(size=1, location=(0.002, 0, BT - 0.005 + 0.0002)); pg1 = bpy.context.object
pg1.scale = (BW - 0.0125, BH - 0.0125, 1); bpy.ops.object.transform_apply(scale=True); obj_mat(pg1, m_pg1); pg1.parent = book
cube('front', (BW, BH, 0.004), (0 - HX, 0, BT - 0.002 - HZ), m_shell, bevel=0.0012, parent=hinge)
cube('spine', (0.006, BH, BT), (-BW / 2 + 0.001, 0, BT / 2), m_shell, bevel=0.0025, parent=book)
for y in (-0.07, 0.07):  # glowing bands on the spine
    cube('band', (0.0066, 0.004, BT - 0.008), (-BW / 2 + 0.001, y, BT / 2), emit('band', CY, 3), parent=book)
bpy.ops.mesh.primitive_plane_add(size=1, location=(0.002 - HX, 0, BT + 0.00015 - HZ)); face = bpy.context.object
face.scale = (BW - 0.008, BH - 0.006, 1); bpy.ops.object.transform_apply(scale=True); obj_mat(face, m_cov); face.parent = hinge
for sx, sy in ((1, 1), (1, -1)):  # metal corner caps on the open edge
    m_cap, nt, b = mat('cap'); setp(b, Base_Color=(0.9, 0.68, 0.34, 1), Metallic=1.0, Roughness=0.22)
    cube('cap', (0.016, 0.016, 0.0052), (sx * (BW / 2 - 0.0075) - HX, sy * (BH / 2 - 0.0075), BT - 0.002 - HZ), m_cap, bevel=0.001, parent=hinge)
book.rotation_euler.z = math.radians(-14); book.location = (0.0, 0.0, 0.0008)

# ---------- hologram above the book ----------
holo = bpy.data.objects.new('holo', None); S.collection.objects.link(holo); holo.location = (0.0, 0.01, 0.185)
m_h = emit('holo', CY, 5); m_hg = emit('hologold', GOLD, 8)
for tilt, rad in ((0, 0.062), (62, 0.062), (-62, 0.062)):
    bpy.ops.mesh.primitive_torus_add(major_radius=rad, minor_radius=0.0006, major_segments=96, location=(0, 0, 0)); o = bpy.context.object
    o.rotation_euler = (math.radians(78), math.radians(tilt), 0); obj_mat(o, m_h); o.parent = holo
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0085, location=(0, 0, 0)); o = bpy.context.object; bpy.ops.object.shade_smooth(); obj_mat(o, emit('core', (1, 0.9, 0.75), 60)); o.parent = holo
for i in range(18):
    a = i / 18 * 2 * math.pi + 0.4
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0032 if i < 5 else 0.0022, location=(0.088 * math.cos(a), 0.088 * math.sin(a), -0.004)); o = bpy.context.object
    obj_mat(o, m_hg if i < 5 else m_h); o.parent = holo
bpy.ops.mesh.primitive_torus_add(major_radius=0.088, minor_radius=0.00025, major_segments=96, location=(0, 0, -0.004)); o = bpy.context.object; obj_mat(o, m_cy_soft); o.parent = holo
holo.rotation_euler = (math.radians(-16), math.radians(6), 0)
for c in list(holo.children): bpy.data.objects.remove(c)
# faint light beam from cover to hologram
m_beam = bpy.data.materials.new('beam'); m_beam.use_nodes = True; nt = m_beam.node_tree; nt.nodes.clear()
outn = nt.nodes.new('ShaderNodeOutputMaterial'); tr = nt.nodes.new('ShaderNodeBsdfTransparent'); emn = nt.nodes.new('ShaderNodeEmission'); addn = nt.nodes.new('ShaderNodeAddShader')
emn.inputs['Color'].default_value = (*CY, 1); emn.inputs['Strength'].default_value = 0.22
lw = nt.nodes.new('ShaderNodeLayerWeight'); lw.inputs['Blend'].default_value = 0.25; mm = nt.nodes.new('ShaderNodeMath'); mm.operation = 'MULTIPLY'; mm.inputs[1].default_value = 0.5
nt.links.new(lw.outputs['Facing'], mm.inputs[0]); nt.links.new(mm.outputs[0], emn.inputs['Strength'])
nt.links.new(tr.outputs[0], addn.inputs[0]); nt.links.new(emn.outputs[0], addn.inputs[1]); nt.links.new(addn.outputs[0], outn.inputs['Surface'])
bpy.ops.mesh.primitive_cone_add(vertices=64, radius1=0.02, radius2=0.085, depth=0.14, location=(0, 0.005, 0.105), end_fill_type='NOTHING'); o = bpy.context.object; bpy.ops.object.shade_smooth(); obj_mat(o, m_beam)
bpy.data.objects.remove(o)

# ---------- light pillars (where Phillis has candles) ----------
m_glass, nt, b = mat('glass'); setp(b, Base_Color=(0.9, 0.95, 1, 1), Roughness=0.08, IOR=1.45); b.inputs['Transmission Weight'].default_value = 1.0
m_base, nt, b = mat('pbase'); setp(b, Base_Color=(0.03, 0.035, 0.05, 1), Metallic=1.0, Roughness=0.3)
for (x, y, h) in ((-0.17, 0.25, 0.105), (-0.105, 0.215, 0.14), (-0.045, 0.27, 0.085)):
    bpy.ops.mesh.primitive_cylinder_add(vertices=6, radius=0.03, depth=h, location=(x, y, h / 2 + 0.012)); o = bpy.context.object
    md = o.modifiers.new('bev', 'BEVEL'); md.width = 0.002; md.segments = 3; obj_mat(o, m_glass); o.rotation_euler.z = random.Random(int(h * 1000)).random()
    bpy.ops.mesh.primitive_cylinder_add(vertices=24, radius=0.0075, depth=h - 0.02, location=(x, y, h / 2 + 0.012)); obj_mat(bpy.context.object, emit('core%d' % int(h * 1000), AMBER, 5)); bpy.ops.object.shade_smooth()
    bpy.ops.mesh.primitive_cylinder_add(vertices=6, radius=0.034, depth=0.012, location=(x, y, 0.006)); o = bpy.context.object; obj_mat(o, m_base); o.rotation_euler.z = 0.3
# glass orb on a ring stand (where Phillis has the wine glass)
ox, oy = 0.15, 0.24
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.058, segments=64, ring_count=32, location=(ox, oy, 0.082)); o = bpy.context.object; bpy.ops.object.shade_smooth(); obj_mat(o, m_glass)
bpy.ops.mesh.primitive_torus_add(major_radius=0.04, minor_radius=0.006, location=(ox, oy, 0.02)); o = bpy.context.object; bpy.ops.object.shade_smooth(); obj_mat(o, m_base)
bpy.ops.mesh.primitive_cylinder_add(radius=0.05, depth=0.01, location=(ox, oy, 0.005)); o = bpy.context.object; obj_mat(o, m_base); bpy.ops.object.shade_smooth()
bpy.ops.mesh.primitive_torus_add(major_radius=0.03, minor_radius=0.0007, location=(ox, oy, 0.082)); o = bpy.context.object; o.rotation_euler = (1.1, 0.3, 0); obj_mat(o, m_h)
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.012, location=(ox, oy, 0.082)); o = bpy.context.object; bpy.ops.object.shade_smooth()
m_mini, nt, b = mat('mini'); setp(b, Base_Color=(0.05, 0.2, 0.5, 1), Emission_Color=(0.1, 0.5, 1, 1), Emission_Strength=2.5); obj_mat(o, m_mini)

# ---------- the window wall ----------
m_wall, nt, b = mat('wall'); setp(b, Base_Color=(0.018, 0.02, 0.03, 1), Metallic=0.8, Roughness=0.4)
WY = 0.95
cube('sill', (5, 0.3, 0.16), (0, WY, 0.0), m_wall, bevel=0.01)
cube('top', (5, 0.3, 0.6), (0, WY, 2.25), m_wall, bevel=0.01)
for x in (-1.25, 1.25): cube('mullion', (0.16, 0.22, 2.4), (x, WY, 1.2), m_wall, bevel=0.02)
cube('sill_light', (5, 0.004, 0.006), (0, WY - 0.152, 0.07), emit('sl', CY, 1.5))

# ---------- the planet ----------
bpy.ops.mesh.primitive_uv_sphere_add(radius=30, segments=160, ring_count=80, location=(14, 78, -22)); pl = bpy.context.object; bpy.ops.object.shade_smooth()
m_pl, nt, b = mat('planet'); tc = nt.nodes.new('ShaderNodeTexCoord')
n1 = nt.nodes.new('ShaderNodeTexNoise'); n1.inputs['Scale'].default_value = 0.09; n1.inputs['Detail'].default_value = 12; n1.inputs['Roughness'].default_value = 0.62
cr = nt.nodes.new('ShaderNodeValToRGB'); e = cr.color_ramp.elements; e[0].position = 0.5; e[0].color = (0.008, 0.045, 0.2, 1); e[1].position = 0.6; e[1].color = (0.16, 0.12, 0.07, 1)
e2 = cr.color_ramp.elements.new(0.54); e2.color = (0.02, 0.16, 0.2, 1)
n2 = nt.nodes.new('ShaderNodeTexNoise'); n2.inputs['Scale'].default_value = 0.16; n2.inputs['Detail'].default_value = 14; n2.inputs['Roughness'].default_value = 0.7
n2.inputs['Distortion'].default_value = 1.2 if 'Distortion' in n2.inputs else 0
cl = nt.nodes.new('ShaderNodeValToRGB'); cl.color_ramp.elements[0].position = 0.56; cl.color_ramp.elements[1].position = 0.8
mx = nt.nodes.new('ShaderNodeMixRGB'); mx.inputs[2].default_value = (0.9, 0.92, 0.95, 1)
nt.links.new(tc.outputs['Object'], n1.inputs['Vector']); nt.links.new(tc.outputs['Object'], n2.inputs['Vector'])
nt.links.new(n1.outputs[0], cr.inputs[0]); nt.links.new(n2.outputs[0], cl.inputs[0]); nt.links.new(cr.outputs[0], mx.inputs[1]); nt.links.new(cl.outputs[0], mx.inputs[0]); nt.links.new(mx.outputs[0], b.inputs['Base Color'])
setp(b, Roughness=0.7); obj_mat(pl, m_pl)
bpy.ops.mesh.primitive_uv_sphere_add(radius=30.5, segments=160, ring_count=80, location=(14, 78, -22)); at = bpy.context.object; bpy.ops.object.shade_smooth()
m_at = bpy.data.materials.new('atmo'); m_at.use_nodes = True; nt = m_at.node_tree; nt.nodes.clear()
outn = nt.nodes.new('ShaderNodeOutputMaterial'); trn = nt.nodes.new('ShaderNodeBsdfTransparent'); df = nt.nodes.new('ShaderNodeBsdfDiffuse'); df.inputs['Color'].default_value = (0.25, 0.55, 1.0, 1)
lw = nt.nodes.new('ShaderNodeLayerWeight'); lw.inputs['Blend'].default_value = 0.12; pw = nt.nodes.new('ShaderNodeMath'); pw.operation = 'POWER'; pw.inputs[1].default_value = 1.6
mxs = nt.nodes.new('ShaderNodeMixShader'); nt.links.new(lw.outputs['Facing'], pw.inputs[0]); nt.links.new(pw.outputs[0], mxs.inputs[0]); nt.links.new(trn.outputs[0], mxs.inputs[1]); nt.links.new(df.outputs[0], mxs.inputs[2]); nt.links.new(mxs.outputs[0], outn.inputs['Surface'])
obj_mat(at, m_at); at.visible_shadow = False

# ---------- lights ----------
def light(kind, name, loc, energy, color, size=0.3, rot=None, target=None):
    d = bpy.data.lights.new(name, kind); d.energy = energy; d.color = color
    if kind == 'AREA': d.size = size
    o = bpy.data.objects.new(name, d); S.collection.objects.link(o); o.location = loc
    if rot: o.rotation_euler = rot
    if target is not None:
        o.rotation_euler = (Vector(target) - Vector(loc)).to_track_quat('-Z', 'Y').to_euler()
    return o
sun = light('SUN', 'sun', (0, 0, 5), 7.0, (1.0, 0.95, 0.9)); sun.data.angle = math.radians(1.5)
sun.rotation_euler = (Vector((0.55, -0.62, -0.42))).to_track_quat('-Z', 'Y').to_euler()   # from behind-left, through the window
light('AREA', 'key', (-0.3, -0.35, 0.55), 9, (1.0, 0.82, 0.62), size=0.5, target=(0, 0, 0.02))
light('AREA', 'fill', (0.6, -0.3, 0.35), 1.2, (0.4, 0.7, 1.0), size=0.6, target=(0, 0.05, 0.05))

# ---------- camera ----------
cd = bpy.data.cameras.new('cam'); cam = bpy.data.objects.new('cam', cd); S.collection.objects.link(cam); S.camera = cam
if VIEW == 'icon' and ICON == 1:
    book.rotation_euler = (math.radians(84), 0, math.radians(-20)); book.location = (0.0, 0.03, BH / 2 + 0.002)
    cd.lens = 50; cam.location = (-0.02, -0.44, 0.15); look = Vector((0.012, 0.0, 0.122))
elif VIEW == 'icon' and ICON == 2:
    cd.lens = 70; cam.location = (0.13, -0.16, 0.15); look = Vector((0.15, 0.24, 0.072))
elif VIEW == 'icon':
    cd.lens = 35; cam.location = (0.02, -0.30, 0.16); look = Vector((0.0, 0.05, 0.065))
elif VIEW == 'phone':
    cd.lens = 30; cam.location = (0.03, -0.50, 0.36); look = Vector((0.0, 0.15, 0.085))
else:
    cd.lens = 30; cam.location = (0.17, -0.50, 0.34); look = Vector((0.14, 0.16, 0.085))
cam.rotation_euler = (look - cam.location).to_track_quat('-Z', 'Y').to_euler()
cd.dof.use_dof = True; cd.dof.focus_distance = (look - cam.location).length if VIEW == 'icon' else (Vector((0, -0.02, 0.03)) - cam.location).length; cd.dof.aperture_fstop = 8
cd.sensor_fit = 'AUTO'
S.render.image_settings.file_format = 'PNG'
focus = bpy.data.objects.new('focus', None); S.collection.objects.link(focus); focus.location = look if VIEW == 'icon' else (0, -0.02, 0.03); cd.dof.focus_object = focus
if MODE in ('open', 'openstill'):
    S.render.fps = FPS; S.frame_start = 1; S.frame_end = F
    bpy.context.view_layer.update()
    page_c = book.matrix_world @ Vector((0.002, 0.0, BT))
    start_loc = cam.location.copy(); q0 = cam.rotation_euler.to_quaternion()
    if VIEW == 'phone': end_loc = page_c + Vector((0.0, -0.105, 0.40))
    else: end_loc = page_c + Vector((0.05, -0.085, 0.27))
    end_look = page_c + (Vector((0, 0.004, 0)) if VIEW == 'phone' else Vector((0.05, 0.0, 0)))
    q1 = (end_look - end_loc).to_track_quat('-Z', 'Y')
    def ease(t): return t * t * (3 - 2 * t)
    for fr in range(1, F + 1):
        t = (fr - 1) / (F - 1); c = ease(t); h = ease(min(1.0, t / 0.72))
        cam.location = start_loc.lerp(end_loc, c); cam.keyframe_insert('location', frame=fr)
        cam.rotation_euler = q0.slerp(q1, c).to_euler(); cam.keyframe_insert('rotation_euler', frame=fr)
        hinge.rotation_euler = (0, -math.radians(168) * h, 0); hinge.keyframe_insert('rotation_euler', frame=fr)
        focus.location = Vector((0, -0.02, 0.03)).lerp(page_c, c); focus.keyframe_insert('location', frame=fr)
    S.render.use_persistent_data = True
    if MODE == 'openstill':
        S.frame_set(int(A.get('frame', F))); S.render.filepath = os.path.abspath(OUT); bpy.ops.render.render(write_still=True)
    else:
        os.makedirs(ANIM, exist_ok=True); S.render.filepath = os.path.join(os.path.abspath(ANIM), 'f####'); S.render.use_overwrite = False
        bpy.ops.render.render(animation=True)
    print('rendered', MODE); sys.exit(0)
S.render.filepath = os.path.abspath(OUT)
bpy.ops.render.render(write_still=True); print('rendered', OUT)
