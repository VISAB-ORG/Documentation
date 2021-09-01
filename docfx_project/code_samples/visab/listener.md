# Creating a SessionListener in VISAB

Due to the fact, that VISABs communication interface is realized with an<br>
event-based HTTP API, the transmission sessions opened by any game need their<br>
very own <code>SessionListener</code> within VISAB that handles the information.

*To understand the inheritance, please have a look into the [code documentation of VISAB](https://visab-org.github.io/api_visab/index.html).*

### Code Sample for Fictive Implementation of Tetris 

```java
package org.visab.processing.tetris;

/**
 * The TetrisListener class, that is responsible for listening to
 * information sent by the Tetris game and creating files with that
 * information.
 */
public class TetrisListener
        extends ReplaySessionListenerBase<TetrisMetaInformation, TetrisStatistics, TetrisImages>
        implements ILiveViewable<TetrisStatistics> {

    private TetrisFile file;

    private List<ILiveViewModel<TetrisStatistics>> viewModels = new ArrayList<>();

    public TetrisListener(UUID sessionId) {
        super(GameName.TETRIS, sessionId);
    }

    @Override
    public void addViewModel(ILiveViewModel<TetrisStatistics> viewModel) {
        viewModels.add(viewModel);

        // If the session isnt active anymore, instantly notify that it was closed.
        if (!isActive)
            notifySessionClosed();
    }

    @Override
    public List<TetrisStatistics> getStatistics() {
        return file.getStatistics();
    }

    @Override
    public void notifySessionClosed() {
        for (var viewModel : viewModels)
            UiHelper.inovkeOnUiThread(() -> viewModel.onSessionClosed());

        viewModels.clear();
    }

    @Override
    public void notifyStatisticsAdded(TetrisStatistics addedStatistics) {
        for (var viewModel : viewModels)
            UiHelper.inovkeOnUiThread(() -> viewModel.onStatisticsAdded(addedStatistics));
    }

    @Override
    public synchronized void onSessionClosed() {
        if (file.getStatistics().size() > 0) {
            var lastStatistics = file.getStatistics().get(file.getStatistics().size() - 1);

            int mostPoints = 0;
            var playerName = "";
            for (var player : lastStatistics.getPlayers()) {
                if (player.getStatistics().getPoints > mostPoints) {
                    playerName = player.getName();
                    mostPoints = player.getStatistics().getPoints();
                }
            }
            file.setWinner(playerName);
        }

        manager.saveFile(file, LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd_HH-mm-ss")),
                sessionId);

        notifySessionClosed();
    }

    @Override
    public void onSessionStarted(TetrisMetaInformation metaInformation) {
        file = new TetrisFile();
        file.setGameSpeed(metaInformation.getGameSpeed());
        file.setMapRectangle(metaInformation.getMapRectangle());
        file.setPlayerCount(metaInformation.getPlayerCount());
        file.getPlayerInformation().putAll(metaInformation.getPlayerInformation());
        file.getPlayerColors().putAll(metaInformation.getPlayerColors());
    }

    @Override
    public synchronized void processImage(TetrisImages mapImage) {
        writeLog(Level.DEBUG, "Received images");
        file.setImages(mapImage);
    }

    @Override
    public synchronized void processStatistics(TetrisStatistics statistics) {
        file.getStatistics().add(statistics);

        writeLog(Level.DEBUG, NiceString.make("has {0} entries now", file.getStatistics().size()));

        notifyStatisticsAdded(statistics);
    }

    @Override
    public IVISABFile getCurrentFile() {
        return file;
    }

    @Override
    public void removeViewModel(ILiveViewModel<TetrisStatistics> viewModel) {
        viewModels.remove(viewModel);
    }
}

```