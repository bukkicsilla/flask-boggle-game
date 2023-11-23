$(function () {
  let score = 0;
  const ColorValue = 180;
  const words = new Set();

  async function storeScore() {
    const res = await axios.post("/store-highscore", { score: score });
    if (res.data.isnewhighscore) {
      $("p").text(`New Record: ${score}`);
    } else {
      $("p").text("Game Over");
    }
  }
  setTimeout(function () {
    $("form input").prop("disabled", true);
    $("form button").prop("disabled", true);
    storeScore();
  }, 30000);

  function getColor() {
    let red = Math.floor(Math.random() * ColorValue);
    let green = Math.floor(Math.random() * ColorValue);
    let blue = Math.floor(Math.random() * ColorValue);
    return `rgb(${red}, ${green}, ${blue})`;
  }

  async function searchWord(event) {
    event.preventDefault();
    let word = $("input").val();
    if (!word) return;
    const res = await axios.get("/search-word", { params: { word: word } });
    const r = res.data.result;
    if (r === "not-word") {
      $("p").text("This word is not in the dictionary");
    } else if (r === "not-on-board") {
      $("p").text("The word is not on the board.");
    } else {
      if (!words.has(word)) {
        $("p").text("You have found a word.");
        score += word.length;
        words.add(word);
      } else {
        $("p").text("You have already checked this word.");
        score -= 1;
      }
      $("h2").text(`Your score: ${score}`);
    }
    $("p").css("color", getColor());
  }

  $("form").on("submit", searchWord);
});
