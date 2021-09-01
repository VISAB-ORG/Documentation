# Closing a session
Session should be closed when the game is done sending data.
If this should not be possible, VISAB also closes sessions automatically after a user defined timeout.
To close a session simply call 
```csharp
await session.CloseSessionAsync();
```

## RoundBasedSession
Very similar to `IVISABSession` we call 
```csharp
await RoundBasedSession.CloseSessionAsync();
```

## LoopBasedSession
Additionally to closing the session, we should also stop the statistics loop.

```csharp
// Stop the infinite statistics loop
cts.Cancel();

await LoopBasedSession.CloseSessionAsync();
```
