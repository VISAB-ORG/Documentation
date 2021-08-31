# Initiating a transmission session

To initiate a transmission session we create a `VISABApi` instance and then call `InitiateSessionAsync`.
```csharp
private async IVISABSession InitiateSession() 
{
    var api = new VISABApi("http://localhost", 2673, 1);
    ...
}
```
The first parameter of the `VISABApi` constructor takes the base adress of the machine that VISAB is running on. If VISAB is running on the same machine as the game, this will be `"http://localhost"`. The second parameter is the port and the third parameter the request timeout (in seconds). If VISAB is running on the same machine, 1 second is more than enough here. If VISAB is running on a machine that isnt in your local network, you'll have to figure out a suitable request timeout.

By creating the `VISABApi` instance, we have not made a call to VISAB yet. When opening a session, VISAB expects us to pass meta information for the session that will be opened. 
```csharp
public class TetrisMetaInformation : IMetaInformation
{
    public string Game => "Tetris";

    public IList<string> PlayerNames { get; set; }

    public int PlayerCount => PlayerNames.Count;
}

private async IVISABSession InitiateSession() 
{
    ...
    var metaInformation = new TetrisMetaInformation 
    { 
        PlayerNames = new List<String> { "Horst", "Dieter" } 
    };
}
```
Lets now open a transmission session for our game by calling `InitiateSessionAsync`.
VISABConnector returns `ApiResponse<T>` objects, where `T` is the type of the content, for every request.
If the `IsSuccess` property is true, the response content can be used as expected.

```csharp
private async IVISABSession InitiateSession() 
{
    ...
    // If we aren't in an asynchronous (async) method, we have to use .Result here
    ApiResponse<IVISABSession> sessionResponse = await api.InitiateSessionAsync(metaInformation);
    if (sessionResponse.IsSuccess)
        return sessionResponse.Content;
    else
        throw new Exception(sessionResponse.ErrorMessage);
}
```

## RoundBasedSession
If we are using the session wrapper class `RoundBasedSession` we can instead use the following code to initiate a session.

```csharp
// Subscribe to the MessageAddedEvent so that we can read the log
RoundBasedSession.MessageAddedEvent += m => Debug.Log(m);

// If we aren't in an asynchronous (async) method, we have to use .Result here
bool success = await RoundBasedSession.StartSessionAsync(metaInformation, "http://localhost", 2673, 1);
if (!success)
    throw new Exception();
```

## LoopBasedSession
The exact same method calls as for `RoundBasedSession`.
```csharp
// Subscribe to the MessageAddedEvent so that we can read the log
LoopBasedSession.MessageAddedEvent += m => Debug.Log(m);

// If we aren't in an asynchronous (async) method, we have to use .Result here
bool success = await LoopBasedSession.StartSessionAsync(metaInformation, "http://localhost", 2673, 1);
if (!success)
    throw new Exception();
```