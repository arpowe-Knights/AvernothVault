
First thing is the Lee is going to make the character and model it around the rig so that when she's done, we simply bind or weight transfer the rig on to Avernoth created character.

Once she makes the model in the shape of the rig she'll send us the asset.

Once we receive the asset we will bind the skeleton to the mesh or weight transfer it. We may have to manully weight paint the character since going from high to low poly but we'll see.

once we do that we send that character into Unreal in it's A or T pose. 

This should allow us to create characters of differing size.

From this point onward all characters will be using this rig and we animate purely the SK_manniquin, using it as like a univerisal rig for all our characters.






# UE5 Mannequin ←→ Blender Animation Workflow

> **Goal:** Animate Unreal Engine 5’s SK_Mannequin in Blender, then export just the animation data back into UE5 and apply it to the original mannequin skeleton.

---

## 1. Export the Mannequin Skeleton from UE5

1. In the **Content Browser**, locate `SK_Mannequin`.
2. Right-click → **Asset Actions → Export…**  
3. Choose **FBX** and save (e.g. `UE5_Mannequin.fbx`).

---

## 2. Import the Mannequin into Blender

1. **File → Import → FBX**  
2. Select `UE5_Mannequin.fbx`.  
3. Verify that:
   - The armature hierarchy matches Unreal’s naming.
   - The mesh (optional) appears but is not strictly required for animation export.

---

## 3. Animate in Blender

- Select the **Armature** object.
- Open the **Action Editor** (Dope Sheet → Action Editor).
- Create and keyframe your custom actions (e.g. Walk, Idle, Custom).
- **Do not** modify bone names or add extra constraints that won’t export cleanly.

---

## 4. Export Only the Animation

1. **File → Export → FBX**  
2. In the FBX Export dialog:
   - **Object Types**  
     - ✔️ Armature  
     - ✔️ Mesh (optional)
   - **Bake Animation**  
     - ✔️ Baked Animation  
     - Frame Start/End: your animation range
   - **Armature**  
     - ❌ Add Leaf Bones (ensure this is **off**)
   - **Path Mode**: Copy  
     - ❌ Embed Textures  

3. Name and export (e.g. `Mannequin_Anim_Walk.fbx`).

---

## 5. Import the Animation into UE5

1. In **Content Browser**, click **Import** and choose `Mannequin_Anim_Walk.fbx`.
2. In the **FBX Import Options**:
   - **Import Mesh**: ❌ off  
   - **Import Animations**: ✔️ on  
   - **Skeleton**: select **SK_Mannequin**  
3. Click **Import**.  
   - A new **Animation Sequence** asset (e.g. `Mannequin_Anim_Walk`) will appear.

---

## 6. Use or Retarget (I'll handle this part mainly but do try to do it yourself just for experience)

- Drop your new Animation Sequence into an **Animation Blueprint** or **Sequencer**.  
- Since it shares the **SK_Mannequin** skeleton, no additional retargeting is required.  
- To retarget to other rigs, set up the Human IK Rig in the **Retarget Manager**.

---

## ⚠️ Tips & Pitfalls

- **Bone Transforms:** Ensure **Apply Transform** is reset so rotations/scales match UE defaults.
- **Leaf Bones:** Disabling “Add Leaf Bones” prevents extra end-bones that break skeleton matching.
- **Mesh Tweaks:** If you ever edit the mannequin mesh itself in Blender, re-export as a new skeletal mesh and reassign animations to its skeleton.

---

