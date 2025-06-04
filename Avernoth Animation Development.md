# UE5 Mannequin ←→ Maya Animation Workflow  

Yea James you literally don't have to read anything else since I found the already rigged Maya file of Manny lol. This document pretty much breaks down the workflow I have to do. Just scroll down to the playlist animations.
The gap in this workflow is that if I don't weight paint properly you animations can be messed up though so keep that in mind when animating. Keep it "stiff"

[[Attachments/Pasted image 20250604030949.png]]

#### Video of Maya workflow
https://www.youtube.com/shorts/2bRF-4QG9AQ

# UE5 Mannequin ←→ Blender Animation Workflow

### **Character Rigging and Animation Workflow**

1. **Modeling Based on Rig**  
    Lee will create the character model, designing it to match the proportions and structure of the universal rig (SK_Mannequin_Manny rig). This ensures compatibility for rig binding and weight transfer later in the process.
    
2. **Asset Delivery**  
    Once the character model is complete and aligned to the rig, Lee will send the asset for integration.
    
3. **Rig Binding and Weight Transfer**  
    Upon receiving the asset, we will bind the rig to the mesh—either through direct binding or weight transfer. Additional weight painting may be necessary to ensure the mesh deforms naturally during animation, avoiding unnatural bending. 
    
4. **Unreal Integration**  
    After rigging, we will export the character in its neutral A-pose or T-pose and import it into Unreal Engine for use.
    
5. **Universal Rig Usage**  
    From this point forward, all characters will use this same rig structure. Animations will be created on the SK_Mannequin and shared across characters of different proportions, treating it as a universal animation rig for the project.

### Oddly Proportioned Characters 
***(pretty much all characters that aren't Manny or Quin)

Incase of the character being in a misaligned pose using the scripts provided in the blender file we can move the bones and orientation (local) 
##### Video on how to do so
https://youtu.be/b1OA6Yq1s0o?si=YhPPzsUUd0echtso


## Export Only the Animation

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


---

## Import the Animation into UE5

1. In **Content Browser**, click **Import** and choose `[AssetName].fbx`.
2. In the **FBX Import Options**:
   - **Import Mesh**: ❌ off  
   - **Import Animations**: ✔️ on  
   - **Skeleton**: Do not select **SK_Mannequin**
3. Click **Import**.  
   - A new **Animation Sequence** asset (e.g. `[AssetName].fbx`) will appear.

4. In the Asset details Window of the Rigged Character's Skeletal Mesh
	    click the drop down that links the Sk_Mannequin Rig essentially saying (These are the same rig)

---

## Retarget Paragon Animations (I'll handle this part mainly but do try to do it yourself just for experience)

### Optional Tips

Since we're using the sk_mannequin we can use the paragon animations as a basis of animations. Paragon was a shutdown epic game that they release all the assets for-for free!

In order to do this we'd have to use retargeting and reanimate in Engine since they use the old UE4 Skeleton 

Updating the skeleton or animation in 3rd party software would make this easy additional help too annoying/inconvenient. So this is a Engine exclusive perk.

#### Video on how to do that incase you want to try it
https://youtu.be/RqfTlAiq23Q?si=nIhUP6XqIq3zoZL6



## Playlist of Potential Animations (Combat)

