# Sendings statistics and images

To send statistics and image data to VISAB we can use our `IVISABSession` object.
The process of sending statistics and images only differs in the extraction phase.
Therefore, the process of sending statistics is exemplary explained.\
For extracting images refer to [Extracting game images](xref:visabconnector_unity.images).

First we create the statistics object based on the current game state.
```csharp
private TetrisStatistics ExtractStatistics(int turn, IList<Player> players) 
{
    var playerPoints = new Dictionary<string, int>();
    foreach (var player in players)
        playerPoints[player.Name] = player.Score;

    var statistics = new TetrisStatistics
    {
        PlayerPoints = playerPoints,
        Turn = turn
    };
}
```

Then we send the statistics object to VISAB.
```csharp
private async void SendStatistics() 
{
    var statistics = ExtractStatistics(...);

    // Assume that the class of this method has a member IVISABSession session.
    // If this is not an asynchronous method, we have to use block by using .Result instead again.
    ApiResponse<string> response = await session.SendStatisticsAsync(statistics);
    if (!response.IsSuccess)
        Debug.Log(response.ErrorMessage);
}
```

## RoundBasedSession

If we are using the `RoundBasedSession` wrapper class, we can simply 
```csharp
await RoundBasedSession.SendStatisticsAsync(statistics);
```

## LoopBasedSession

In real-time based games, we likely want to send statistics in time intervals.
To achieve this without much effort, we can use `LoopBasedSession.StartStatisticsLoopAsync`.

`StartStatisticsLoopAsync` expects a `Func<IStatistics>` using which the statistics object is generated. The function which we will encapsulate could look like this.
```csharp
public class PlayerStatistics
{
    public int Kills { get; set; }

    public int Deaths { get; set; }
}

public class ShooterStatistics : IStatistics
{
    public IDictionary<string, PlayerStatistics> PlayerStatistics { get; set; }
}

private ShooterStatistics StatisticsFunc(IList<Player> players)
{
    var playerStatistics = new Dictionary<string, PlayerStatistics>();
    foreach (var player in players) 
    {
        playerStatistics[player.Name] = new PlayerStatistics { 
            Kills = player.Kills, 
            Deaths = player.Deaths 
        };
    }

    return new ShooterStatistics { PlayerStatistics = playerStatistics };
}
```
`StartStatisticsLoopAsync` also expects
* A `Func<bool>` that is evaluated to check if statistics should be extracted and sent
* The interval in which statistics should be sent in miliseconds
* A `CancellationToken` instance, that is evaluted to check if the inifinite loop of sending statistics should be stopped.

Combining this with the `StatisticsFunc` we created already, we can start the statistics loop like this.
```csharp
private void StartStatisticsLoop() 
{
    // Assume the class of our method has a member CancellationTokenSource cts.
    cts = new CancellationTokenSource();
    Func<bool> shouldSend = () => true;

    // StartStatisticsLoopAsync is an async void method, which is why we cannot await it, use .Result, or .Wait().
    LoopBasedSession.StartStatisticsLoopAsync(StatisticsFunc, shouldSend, 100, cts.Token);
}
```

