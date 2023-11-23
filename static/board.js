$(function () {
  const form = document.querySelector("form");
  //const inputEl = document.querySelector("input");
  //const paragEl = document.querySelector("p");
  //const h2El = document.querySelector("h2");
  //const table = document.querySelector("table");
  let score = 0;
  const ColorValue = 180;
  const words = new Set();

  setTimeout(function () {
    //paragEl.innerText = "Game Over";
    $("p").text("Game Over");
    $("form input").prop("disabled", true);
    $("form button").prop("disabled", true);
  }, 60000);

  function getColor() {
    let red = Math.floor(Math.random() * ColorValue);
    let green = Math.floor(Math.random() * ColorValue);
    let blue = Math.floor(Math.random() * ColorValue);
    return `rgb(${red}, ${green}, ${blue})`;
  }
  /*async function searchWord(event) {
    event.preventDefault();
    let word = inputEl.value;
    if (!word) return;
    //axios.get("/search-word?word=moon")
    const res = await axios.get("/search-word", { params: { word: word } });
    console.log(res.data.result);
    const r = res.data.result;
    if (r === "not-word") {
      paragEl.innerText = "This word is not in the dictionary.";
    } else if (r === "not-on-board") {
      paragEl.innerText = "The word is not on the board.";
    } else {
      paragEl.innerText = "You have found a word.";
      score += word.length;
      h2El.innerText = `Score: ${score}`;
    }
    paragEl.style.color = getColor();
  }*/
  async function searchWord(event) {
    event.preventDefault();
    let word = $("input").val();
    console.log(word);
    if (!word) return;
    const res = await axios.get("/search-word", { params: { word: word } });
    const r = res.data.result;
    if (r === "not-word") {
      $("p").text("This word is not in the dictionary");
    } else if (r === "not-on-board") {
      $("p").text("The word is not on the board.");
    } else {
      //$("p").text("You have found a word.");
      if (!words.has(word)) {
        $("p").text("You have found a word.");
        score += word.length;
        //$("h2").text(`Score: ${score}`);
        words.add(word);
      } else {
        $("p").text("You have already checked this word.");
        score -= 1;
        //$("h2").text(`Score: ${score}`);
      }
      $("h2").text(`Score: ${score}`);
    }
    $("p").css("color", getColor());
  }

  form.addEventListener("submit", searchWord);
});
