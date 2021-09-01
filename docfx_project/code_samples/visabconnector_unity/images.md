---
uid: visabconnector_unity.images
---

# Extracting game images

Say we need to snapshot three different kinds of blocks for our Tetris game, also the game canvas itself. 

First of all we have to decide if it is viable, to instantiate the desired game objects or not. Generally speaking, it makes sense to instantiate game objects outside of the game's main view, when they will spawn rather erratically. So in our case we don't know when Tetris will spawn each block and since we need the snapshots at the start of a game session, it is advisable to instantiate them rather than trying to snapshot out of the running game. 

The following shows how we would set up the configuration for game objects that will be instantiated. What we need for that is the path to the Prefab (template for game objects). The spawn location can be set manually and should be outside of the main camera's view. 

```csharp
private TetrisImages TakeSnapshots() 
{
    Func<string, SnapshotConfiguration> defaultInstantiate = (prefabPath) => new SnapshotConfiguration 
    { 
        ImageHeight = 1024, 
        ImageWidth = 1024, 
        InstantiationSettings = new InstantiationConfiguration 
        { 
            PrefabPath = prefabPath, 
            SpawnLocation = new Vector3(100, 100, 100), 
        }, 
        CameraConfiguration = new CameraConfiguration 
        { 
            CameraOffset = 1.5f, 
            Orthographic = false, 
            UseAbsoluteOffset = false, 
            CameraRotation = new Vector3(90, 0, 0) 
        } 
    };
    ...
}
``` 

Next, we need to declare which game objects we want to snapshot. The following code sample shows how you can do that by creating a dictionary. Other than that, we can also define the prefab path in the configuration function itself (under `PrefabPath`). This allows us to configure for only one game object. 
```csharp
private TetrisImages TakeSnapshots() 
{
    ...
    var bricks = new Dictionary<string, string> 
    { 
        { "Big Brick", "Prefabs/Big_Brick" }, 
        { "Small Brick", "Prefabs/Small_Brick" }, 
        { "L Shape", "Prefabs/L_Brick" }, 
    }; 
}
``` 
In this case we are going to snapshot three different brick shapes, which are stored in said dictionary together with their prefab paths (values). 

Finally we need to conduct the actual snapshotting by invoking the `TakeSnapshot` method from the `ImageCreator` class. As displaced in the code sample below, this will be done by iterating through the bricks dictionary and passing the values as parameters to the configuration function. The returned image bytes will be added to the image container that has predefined placeholders for each image type that needs to be snapshotted for the specific game. In this case the brick shapes will be stored in the OneOneOneOne byte array.
```csharp
private TetrisImages TakeSnapshots() 
{
    ...
    var images = new TetrisImages();
    foreach (var pair in bricks) 
    { 
        var config = defaultInstantiate(pair.Value); 
        var bytes = ImageCreator.TakeSnapshot(config); 
        images.OneOneOneOne = bytes;
    }
}
```
# TODO: Either adapt `TetrisImages` class or adapt the example.