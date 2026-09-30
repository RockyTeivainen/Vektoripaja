<div style="background-color: #000000; color: #89CFF0; padding: 30px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6;">

# Low-Poly Vector 3D Modeling Tool
## System Architecture & Technical Specification Documentation

---

<h2 style="color: #89CFF0; border-bottom: 1px solid #89CFF0; padding-bottom: 4px;">1. Vision & Core Philosophy</h2>

This project aims to bridge the gap between 2D vector graphic design (specifically Inkscape's node-based workflows) and low-poly 3D modeling[cite: 5]. 

### Core Tenets
* <strong style="color: #89CFF0;">No Traditional Mesh Editing:</strong> Bypasses traditional vertex-edge-face extrusion and box-modeling paradigms[cite: 5].
* <strong style="color: #89CFF0;">Vector-Driven Surface Generation:</strong> Models are defined and modified by drawing, lofting, revolving, and combining 2D/3D Bezier vector curves[cite: 5].
* <strong style="color: #89CFF0;">Low-Poly Procedural Native:</strong> Geometry is procedurally generated from parametric profiles and curves, optimized for clean `.obj` exports[cite: 5].
* <strong style="color: #89CFF0;">Non-Destructive & Hierarchical:</strong> Shapes remain editable via their underlying vector paths throughout the entire design process[cite: 5].
* <strong style="color: #89CFF0;">Accessibility & High Precision:</strong> Focuses on spacious 2D vector precision without cluttering the screen with tiny multi-pane viewports.

---

<h2 style="color: #89CFF0; border-bottom: 1px solid #89CFF0; padding-bottom: 4px;">2. Toolset Architecture</h2>

### 2.1 General Tools
* <strong style="color: #89CFF0;">Selection Tool:</strong> Selects, translates, rotates, and scales whole objects/sub-meshes in 3D space[cite: 5].

### 2.2 Path & Lofting Tools
* <strong style="color: #89CFF0;">Edit by Nodes (Vertex & Edge Tool):</strong> Inkscape-style node editing for 2D and 3D paths[cite: 5]. Supports inserting nodes between selected vertices, deleting nodes, adjusting handle tangents, and snapping[cite: 5].
* <strong style="color: #89CFF0;">3D Bezier Pen Tool:</strong> Draws vector paths in 3D space across orthographic or perspective planes with 3D Bezier control handles[cite: 5].
* <strong style="color: #89CFF0;">Cross-Section Sweeping ("Stroke-to-Solid"):</strong> Assigns a 2D profile (e.g., triangular tube, square tube, flat ribbon) along a Bezier path with an adjustable **Segment Count** slider (3–8 sides) to generate volumetric stroke geometry dynamically[cite: 5].
* <strong style="color: #89CFF0;">Revolve (Lathe) Tool:</strong> Generates rotational 3D solids by sweeping a half-profile 2D vector sketch around a designated axis (e.g., $Y$-axis centerline). Features parametric controls for `Sweep Angle` ($0^\circ–360^\circ$), `Radial Segment Steps` (e.g., 3–32 steps for low-poly faceting), and `Axis Offset`. Ideal for symmetrical objects like vases, cups, barrels, domes, and wheels.

### 2.3 Solid Primitive Tools
Tools that directly generate volumetric geometry:
* <strong style="color: #89CFF0;">Rectangular Prism:</strong> Defined parametrically by `Width`, `Height`, and `Depth`[cite: 5].
* <strong style="color: #89CFF0;">Sphere:</strong> Defined parametrically by `Radius` and base tessellation steps[cite: 5].
* <strong style="color: #89CFF0;">Pyramid:</strong> Defined parametrically by `Base Shape` (<em>Circle</em>, <em>Rectangle</em>, or <em>Equilateral Triangle</em>), `Base Area`, and `Height`[cite: 5].
* <strong style="color: #89CFF0;">Platonic Solids Tool:</strong> Parametrically generates regular convex polyhedra by selecting `Type` (<em>Tetrahedron</em>, <em>Cube/Hexahedron</em>, <em>Octahedron</em>, <em>Dodecahedron</em>, or <em>Icosahedron</em>) and `Scale/Radius`.
* <strong style="color: #89CFF0;">Trapezohedron Tool:</strong> Parametrically generates $n$-gonal trapezohedra (duals of antiprisms) defined by `Degree` ($n$-gon base, e.g., trigonal, tetragonal, pentagonal), `Radius`, and `Height/Asymmetry`.

---

<h2 style="color: #89CFF0; border-bottom: 1px solid #89CFF0; padding-bottom: 4px;">3. Viewport Navigation & Canvas Interface</h2>

Designed to maximize screen real estate for precise vector node editing while allowing full 3D camera exploration:

### 3.1 Hybrid Viewport Modes
* <strong style="color: #89CFF0;">Single Viewport Default:</strong> The default layout presents a single, spacious workspace maximizing real estate for node editing.
* <strong style="color: #89CFF0;">Picture-in-Picture (PiP) Overlay:</strong> A small, resizable corner preview window displays the live 3D rendered volume while drawing on the main 2D orthographic canvas. Clicking the PiP window swaps the 2D and 3D views instantly.
* <strong style="color: #89CFF0;">Optional Viewport Splitting:</strong> Supports side-by-side split screens with adjustable, thick drag-and-drop splitter bars.

### 3.2 Camera Control & View Lock System
* <strong style="color: #89CFF0;">Free 3D Orbit:</strong> Users can freely orbit, tilt, pan, and zoom around the model in 3D space.
* <strong style="color: #89CFF0;">Orthographic Plane Snap:</strong> Clicking an axis on the Orientation Gizmo snaps the camera flat to cardinal planes (Front, Left, Top).
* <strong style="color: #89CFF0;">Universal View Lock Toggle:</strong> A quick UI toggle button (and hotkey) that completely freezes camera rotation at **any arbitrary angle or perspective view** (not restricted to orthographic planes). When locked, navigation inputs on the canvas are restricted to 2D panning and vector node editing, preventing accidental camera rotation during fine drawing operations.
* <strong style="color: #89CFF0;">Transition Style Settings:</strong> Offers user-selectable camera transitions between **Smooth Orbit Interpolation** and **Instant Cut Snap**.
* <strong style="color: #89CFF0;">Infinite Vector Zoom & Accessibility:</strong> Zooming in close maintains crisp, resolution-independent vector lines and enlarged node control handles for high visual accessibility.

---

<h2 style="color: #89CFF0; border-bottom: 1px solid #89CFF0; padding-bottom: 4px;">4. Orthographic Lofting & Mesh Generation Workflow</h2>

Generating complex 3D forms from 2D profile paths relies on an orthographic cross-section lofting pipeline[cite: 5]:

<pre style="background-color: #111111; color: #89CFF0; border: 1px solid #89CFF0; padding: 12px; border-radius: 4px; overflow-x: auto;">
  ┌──────────────────┐      ┌──────────────────┐      ┌─────────────────────┐
  │ Primary Profile  │  ──► │ Orthographic     │  ──► │ Volume Lofting &    │
  │ (e.g. Front View)│      │ Alignment Guides │      │ Refinement Curves   │
  └──────────────────┘      └──────────────────┘      └─────────────────────┘
</pre>

### 4.1 Primary Contour & Depth Profiling
1. <strong style="color: #89CFF0;">First Profile:</strong> User draws a 2D closed/open profile on a cardinal view (e.g., Front View)[cite: 5].
2. <strong style="color: #89CFF0;">Depth Profile:</strong> User switches to a perpendicular view (e.g., Side/Left View) and draws depth-defining curves[cite: 5].
3. <strong style="color: #89CFF0;">Volume Triggering:</strong> Volume can be generated automatically upon detecting a valid curve set, or manually via a keyboard shortcut/UI button[cite: 5].

### 4.2 Automatic Orthographic Bounding & Alignment Snapping
To prevent topological gaps and non-manifold geometry[cite: 5]:
* <strong style="color: #89CFF0;">Projection Guides:</strong> Switching views automatically projects thin, ghosted reference lines and bounding extents of the primary profile[cite: 5].
* <strong style="color: #89CFF0;">Node Snapping:</strong> Start and end points of depth curves snap directly to projected boundary markers, ensuring exact alignment across axes[cite: 5].

---

<h2 style="color: #89CFF0; border-bottom: 1px solid #89CFF0; padding-bottom: 4px;">5. SVG Layer Parser & Automatic Assembly</h2>

### 5.1 Structural Mapping & Layer Extraction
The importer parses SVG document tree structures (`<g>` groups and nested layers) and maps them directly into a 3D Scene Graph parenting hierarchy:

<pre style="background-color: #111111; color: #89CFF0; border: 1px solid #89CFF0; padding: 12px; border-radius: 4px; overflow-x: auto;">
SVG Group Hierarchy                    3D Scene Graph
├── Layer 1: Torso                 ──►  Root Mesh (Torso)
│   ├── Sub-layer: Head            ──►  Child Mesh (Head, parented to Torso)
│   │   ├── Sub-layer: Ears        ──►  Grandchild Mesh (Ears, parented to Head)
│   │   └── Sub-layer: Muzzle      ──►  Grandchild Mesh (Muzzle, parented to Head)
│   └── Sub-layer: Near_Leg        ──►  Child Mesh (Near_Leg, parented to Torso)
</pre>

* <strong style="color: #89CFF0;">Global Coordinate Preservation:</strong> Vector paths retain their shared 2D canvas coordinates $(X, Y)$ across all layers upon extraction, preventing manual 3D re-assembly.
* <strong style="color: #89CFF0;">Layer Stacking to Z-Depth Mapping:</strong> SVG rendering layer order (top-to-bottom) maps directly to default initial 3D Z-depth offsets ($+Z$ for front layers, $-Z$ for back layers).
* <strong style="color: #89CFF0;">Surface Socket Auto-Generation:</strong> Overlapping junction points automatically initialize Surface Socket Pivots at parent-child intersection centroids.

---

<h2 style="color: #89CFF0; border-bottom: 1px solid #89CFF0; padding-bottom: 4px;">6. Volumetric Inflation Algorithms</h2>

### 6.1 Medial Axis Sphere Inflation (Cranium & Muzzle Topology)
For organic geometry with varying regional volume (such as a round head connected to a tapering snout), the engine utilizes **Medial Axis (Maximal Inscribed Circle) Inflation**:

1. **Skeleton Extraction:** Computes the interior Medial Axis Transform (MAT) from the closed 2D boundary path.
2. **Inscribed Radius Sampling:** Calculates the maximum inscribed radius $R(t)$ touching the contour boundary at every point along the axis.
3. **Implicit Surface Sweeping:** Generates a smooth 3D isosurface skin around the sphere field defined by $R(t)$ (large spherical skull core tapering continuously into the muzzle).

<pre style="background-color: #111111; color: #89CFF0; border: 1px solid #89CFF0; padding: 12px; border-radius: 4px; overflow-x: auto;">
2D Profile Outline            Medial Axis & Radii              3D Volumetric Mesh
┌──────────────────┐         ┌────────────────────┐           ┌───────────────────┐
│   ◯ Head Core    │  ──►    │  R1 (Large Sphere) │    ──►    │ Smooth 3D Head    │
│     \ Muzzle     │         │    \ R2..R3 Taper  │           │ Integrated Muzzle │
└──────────────────┘         └────────────────────┘           └───────────────────┘
</pre>

### 6.2 Dual-Axis Sweep (Paws & Tapered Limbs)
1. **Centerline Spine Extraction:** Derives a 1D skeleton curve along the longitudinal axis of the 2D limb sketch.
2. **Variable Elliptical Cross-Sectioning:** At each point $s$ along the spine, an elliptical slice is evaluated:
   $$\text{Radius}_Z(s) = \text{Distance from spine to Side Profile boundary at } s$$
   $$\text{Radius}_X(s) = \begin{cases} \text{Radius}_Z(s) \times k_{\text{width}} & \text{if Mode = Derived} \\ \text{Distance to Front Profile at } s & \text{if Mode = Custom Sketch} \end{cases}$$
3. **Skinning:** Sweeps continuous quad/triangle topology across all elliptical cross-sections to generate clean limb and paw geometry.

---

<h2 style="color: #89CFF0; border-bottom: 1px solid #89CFF0; padding-bottom: 4px;">7. Profile Binding Channels & Multi-Axis Geometry</h2>

### 7.1 Non-Destructive Profile Binding Architecture
To support 1-click conversion while enabling multi-view geometric control, each sub-component exposes three independent **Profile Binding Channels**: $X$-Width, $Y$-Height, and $Z$-Depth.

### 7.2 Binding Modes per Channel
1. **`Follow Sketch [Path_ID]` (Primary Default):** Directly bound to the active 2D vector path drawn or imported in that view projection.
2. **`Derived` (Zero-Error Fallback):** Automatically computes profile thickness along the orthogonal axis based on the primary sketch dimensions ($\text{Radius}_X = \text{Radius}_Z \times \text{Width Multiplier}$). Guarantees immediate 3D volume without producing flat or zero-thickness errors.
3. **`Custom Sketch` (Manual Override):** Replaces the `Derived` fallback with explicit 2D vector data drawn on a perpendicular reference plane (e.g., Front View).

---

<h2 style="color: #89CFF0; border-bottom: 1px solid #89CFF0; padding-bottom: 4px;">8. Multi-Shape Hierarchy & Assembly</h2>

Complex subjects (e.g., character models) are built by assembling simpler component sub-meshes rather than stitching a single complex outline[cite: 5].

<pre style="background-color: #111111; color: #89CFF0; border: 1px solid #89CFF0; padding: 12px; border-radius: 4px; overflow-x: auto;">
                   ┌──────────────┐
                   │  Torso Mesh  │  (Root Parent)
                   └──────┬───────┘
                          │
            ┌─────────────┴─────────────┐
            ▼                           ▼
     ┌─────────────┐             ┌─────────────┐
     │  Head Mesh  │             │  Leg Mesh   │
     └──────┬──────┘             └─────────────┘
            │
            ▼
     ┌─────────────┐
     │  Ear Mesh   │
     └─────────────┘
</pre>

### 8.1 Component-Based Grouping
* Shapes are broken down into self-contained sub-objects (e.g., <em>Head</em>, <em>Torso</em>, <em>Limbs</em>)[cite: 5].
* Sub-shapes overlap naturally in 3D space without requiring continuous skin-stitching algorithms[cite: 5].

### 8.2 Surface-Anchored Joint Sockets
* <strong style="color: #89CFF0;">Root Profile Tapering:</strong> Child sub-shapes automatically taper slightly at their connection rim, forming a clean joint transition instead of harsh geometric clipping[cite: 5].
* <strong style="color: #89CFF0;">Z-Fighting Prevention:</strong> A minute scale/depth offset (1–2%) is applied at connection planes to eliminate flickering textures[cite: 5].

---

<h2 style="color: #89CFF0; border-bottom: 1px solid #89CFF0; padding-bottom: 4px;">9. Parenting, Surface Locking & Collision Rules</h2>

To maintain logical placement during manipulation and prevent clipping errors[cite: 5]:

### 9.1 Parent-Child Linking & Sockets
* Users select elements and assign relationships (e.g., <em>Ear</em> &rarr; <em>Head</em> &rarr; <em>Torso</em>)[cite: 5].
* <strong style="color: #89CFF0;">Automatic Socket Pivots:</strong> Linking automatically places the child's rotation pivot at the intersection point with the parent's surface, aligned to the surface normal[cite: 5].

### 9.2 Hierarchy-Aware Raycasting
* <strong style="color: #89CFF0;">Direct Parent Magnetism:</strong> Raycasting for surface attachment only registers the designated direct parent mesh, ignoring unrelated sub-shapes[cite: 5].
* <strong style="color: #89CFF0;">Collision Filters:</strong> Paws, tails, and opposing limbs do not stick to or sink into each other[cite: 5].
* <strong style="color: #89CFF0;">Bounding Volume Bumping:</strong> Unrelated sub-objects utilize simplified bounding spheres to prevent physical clipping through adjacent limbs[cite: 5].

### 9.3 Surface Lock & Parametric Adaptability (UV Surface-Binding)
* <strong style="color: #89CFF0;">Relative Coordinate Binding:</strong> Child locations are stored as normalized surface coordinates $(U, V)$ relative to the parent's contour paths[cite: 5].
* <strong style="color: #89CFF0;">Dynamic Morph Adaptability:</strong> Modifying the parent's base vector nodes automatically shifts attached children along the updated surface, preserving alignment without floating or clipping[cite: 5].

---

<h2 style="color: #89CFF0; border-bottom: 1px solid #89CFF0; padding-bottom: 4px;">10. Mesh Pipeline & Export Specifications</h2>

### 10.1 Dynamic Mesh State
* <strong style="color: #89CFF0;">Active Curve Stack:</strong> Refinement curves are managed non-destructively in an ordered stack (`Base Profile` &rarr; `Curve A` &rarr; `Curve B`)[cite: 5]. Curves can be toggled, reordered, or deleted[cite: 5].
* <strong style="color: #89CFF0;">Live Parametric Mesh:</strong> Mesh geometry updates procedurally in real-time as underlying vector nodes are edited[cite: 5].

### 10.2 Export Paradigms (.OBJ Format)

<table style="width: 100%; border-collapse: collapse; margin-top: 10px; color: #89CFF0; border: 1px solid #89CFF0;">
  <thead>
    <tr style="background-color: #111111; border-bottom: 1px solid #89CFF0;">
      <th style="padding: 10px; text-align: left; border-right: 1px solid #89CFF0;">Export Option</th>
      <th style="padding: 10px; text-align: left; border-right: 1px solid #89CFF0;">Mechanics</th>
      <th style="padding: 10px; text-align: left;">Primary Use Case</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #333333;">
      <td style="padding: 10px; font-weight: bold; border-right: 1px solid #89CFF0;">Modular Sub-Meshes (Default)</td>
      <td style="padding: 10px; border-right: 1px solid #89CFF0;">Keeps sub-shapes as separate distinct geometries (`o Head`, `o Leg`) inside a single file[cite: 5].</td>
      <td style="padding: 10px;">Rigging, animation, game engine imports, easy re-editing[cite: 5].</td>
    </tr>
    <tr>
      <td style="padding: 10px; font-weight: bold; border-right: 1px solid #89CFF0;">Fused Boolean Union</td>
      <td style="padding: 10px; border-right: 1px solid #89CFF0;">Merges overlapping volumes into a single continuous manifold skin, stripping internal faces[cite: 5].</td>
      <td style="padding: 10px;">3D printing (watertight requirement), physics colliders, sculpting bases[cite: 5].</td>
    </tr>
  </tbody>
</table>

</div>