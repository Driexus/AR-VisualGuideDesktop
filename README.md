
# AR-VisualGuide Desktop

AR-VisualGuide is a prototype application developed mainly in Unity for use in Android, which aims to provide visitors of the Archeological Museum of Thessaloniki navigational assistance and information about the various exhibits. 

This application was the main objective of a thesis for the Electrical and Computer Engineering degree, which may be found **here**. 

This project is a part of a bigger project which may be found [here](https://github.com/Driexus/AR-VisualGuide).


## How to use
1. Clone the repo and place a file named "appConfig.ini" in the root folder containing the details specified later in this document. If you are using this app for an existing project you should ask for the file.
2. Navigate to or create a new project using the [create_project.py](https://github.com/Driexus/AR-VisualGuideDesktop/blob/main/create_project.py) script.
3. Edit the "config.ini" file inside the project folder (as specified below) to include the vuforia keys or request the file for an already existing project.
4. Create or open a blender file inside the project folder and using vertices and edges mark walls in 2d coordinates using real-life scale. The walls should be placed under an object named "Walls".
5. Place items and image targets in the correct coordinates under collections named "Items" and "Targets" respectively. Each item's and target's name should be the same as the id they are registered with in Firebase. 
	> Items do not have an orientation. Targets' orientation should be changed to "YXZ" to appear correctly in Unity.
6. From inside the Blender file (using the Blender Python API) run the [write_blender_data_to_csv.py](https://github.com/Driexus/AR-VisualGuideDesktop/blob/main/write_blender_data_to_csv.py) script to update the csv files holding the data of the scene.
7. Run the [upload_blender_data.py](https://github.com/Driexus/AR-VisualGuideDesktop/blob/main/upload_blender_data.py) script in order to upload the information found in the csv files to Firebase.
	> Writing to Firebase in this manner is a set instruction, meaning previous data will be overwritten without warning. If you are unsure about this operation it is advised to backup the files in Firebase using the export utility that is provided in its dashboard.



## Config formatting

config.ini:
```
[FIREBASE]
buildingid = {a random id}

[VUFORIA]
accessKey = {public vuforia key}
secretKey = {secret vuforia key}
```

appConfig.ini:
```
[FIREBASE]
apiKey = {api key}
authDomain = {auth domain}
databaseURL = {database URL}
storageBucket = {storage bucket}
username = {username}
password = {password}
```

