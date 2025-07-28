# UE5 Mannequin ←→ Maya Animation Workflow  

Yea James you literally don't have to read anything else since I found the already rigged Maya file of Manny lol. This document pretty much breaks down the workflow I have to do. Just scroll down to the playlist animations.
The gap in this workflow is that if I don't weight paint properly you animations can be messed up though so keep that in mind when animating. Keep it "stiff"

![Pasted image 20250604030949](Attachments/Pasted%20image%2020250604030949.png)


#### Video of Maya workflow
https://www.youtube.com/shorts/2bRF-4QG9AQ

#### Assets Maya
https://gumroad.com/d/a22ff08b4944d74c7733c439c83a8a94


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

Alternatively we just import them into Cascadeur



# Even more animation info 

So while struggling to fix the corrupted rig in Cascadeur I've been learning more about the software itself. 

### Here are a few workflow tips I think will help

- In Cascadeur there are this points called Fulcrum points essentially it's the points that come into contact with a surface (on our case the ground). These are important for the autophyics feature in Cascadeur as certain motions can be made to indicate to the physics to jump or to lean character weight to one leg or the other.

**Here's a short video explaining Fulcrums**
https://youtu.be/oKfrD1GJ0qU?si=dyO1X-NQOfALsI8t&t=179

- Using Mixamo Animations And Mocap works a little weird in Cascadeur. You can't directly send animations into Cascadeur because It has no retargeting software for non Pro Users. The workaround is to 
1. First Create a scene with a UE5 Character
2. Export the character with only Object Selected should look like this:
   ![[Attachments/Pasted image 20250708233034.png]]
3. Once you export the the character take it to mixamo, find the animation you want, and upload the Character FBX you exported I name mine "MannyCAS.fbx"
4. Once your character upload you now want to export that character from mixamo without the character so purely the animation this step is important.
	- It's important because Mixamo retargets the animation to the character's Rig so when you bring it to Cascadeur or Unreal there will be no issues with the joint hierarchy naming. 
	- Exporting with the character skin attach will cause unpredictable behavior with animations and animation transfers 
5. Once that's done make a new scene in Cascadeur and drag the Animation Fbx that you got from mixamo. 
6. The scene will look empty until you switch the scene mode
![[Attachments/Pasted image 20250708233753.png]]
Click the arrow next to the respective posing mode and select the "joint" mode
![[Attachments/Screenshot 2025-07-08 233841.jpg]]

7. Select All the joints and all the keyframes of the animation scene and click "**copy interval**" 
![[Attachments/Pasted image 20250708234215.png]]

8. Good back to the scene with UE5 Manny or Quin highlight/select all the joints Hit paste interval and boom! You have a basis for animation you can tinker with. Add in-betweens using "SHIFT+" or Remove them with "SHIFT-". Delete keyframes whatever you want. 
![[Attachments/Pasted image 20250708234527.png]]

**Video On how to this** lol

https://youtu.be/SZHVubEDifk?si=lQX4A_5gfCe8AYsQ


## How to kill Trajectory (use as needed)

In the copier chose which axis you need
![[../Pasted image 20250709125349.png]]

Make sure the object says center of mass 
![[../Pasted image 20250709151239.png]]

Next hover over the edit dropdown to select paste into the interval 
![[../Pasted image 20250709150859.png]]

The interval is the time line at the bottom with the key frames. Make sure you select the exact area or the entire timeline of the animation. 
This will kill the trajectory so that the animation stays in place 


## Cascadeur Tips when animating video

https://youtu.be/EefecntjXdk

## Animations to reference video

https://youtu.be/FmMjujPuD3k