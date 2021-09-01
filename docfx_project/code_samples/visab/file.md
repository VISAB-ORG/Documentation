# Creating a Game File in VISAB

Information sent by the respective game will be deserialized from JSON and written into<br>
a file, so that it can be visualized afterwards. To handle this content appropriately these<br>
game-specific files need their very own implementation in VISAB.

*To understand the inheritance, please have a look into the [code documentation of VISAB](https://visab-org.github.io/api_visab/index.html).*

### Code Sample for Fictive Implementation of Tetris 

```java
package org.visab.globalmodel.Tetris;

/**
 * Represents the Tetris VISAB file containing that contains all information necesarry
 * for visualizing. This class is serialized to json and written to .visab
 * files.
 */
public class TetrisFile extends BasicVISABFile {

    private List<TetrisStatistics> statistics = new ArrayList<>();
    private int playerCount;
    private Rectangle mapRectangle;
    private Map<String, String> playerInformation = new HashMap<>();
    private float gameSpeed;
    private Map<String, String> playerColors = new HashMap<>();
    private TetrisImages images;
    private String winner;

    public TetrisFile() {
        super(GameName.TETRIS, "2.0");
    }

    public String getWinner() {
        return winner;
    }

    public void setWinner(String winner) {
        this.winner = winner;
    }

    public TetrisImages getImages() {
        return images;
    }

    public void setImages(TetrisImages images) {
        this.images = images;
    }

    public Map<String, String> getPlayerColors() {
        return playerColors;
    }

    public void setPlayerColors(Map<String, String> playerColors) {
        this.playerColors = playerColors;
    }

    public List<TetrisStatistics> getStatistics() {
        return statistics;
    }

    public int getPlayerCount() {
        return this.playerCount;
    }

    public void setPlayerCount(int playerCount) {
        this.playerCount = playerCount;
    }

    public Rectangle getMapRectangle() {
        return this.mapRectangle;
    }

    public void setMapRectangle(Rectangle mapSize) {
        this.mapRectangle = mapSize;
    }

    public Map<String, String> getPlayerInformation() {
        return this.playerInformation;
    }

    public float getGameSpeed() {
        return this.gameSpeed;
    }

    public void setGameSpeed(float gameSpeed) {
        this.gameSpeed = gameSpeed;
    }

    public List<String> getPlayerNames() {
        return new ArrayList<>(playerInformation.keySet());
    }

}

```