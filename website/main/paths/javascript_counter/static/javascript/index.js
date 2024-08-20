// Counter Program

const decreaseButton = document.getElementById("decreaseButton")
const resetButton = document.getElementById("resetButton")
const increaseButton = document.getElementById("increaseButton")
const counterLabel = document.getElementById("counterLabel")

increaseButton.onclick = function(){
    count++;
    counterLabel.textContent = count;
}
decreaseButton.onclick = function(){
    count--;
    counterLabel.textContent = count;
}
resetButton.onclick = function(){
    count = 0;
    counterLabel.textContent = count;
}