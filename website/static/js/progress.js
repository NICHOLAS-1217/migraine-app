// Select all elements with the class "circular-progress"
let circularProgressList = document.querySelectorAll(".circular-progress");

// Loop through each circular progress element
circularProgressList.forEach(circularProgress => {
    let progressValue = circularProgress.querySelector(".progress-value");

    let progressStartValue = 0,
        progressEndValue = parseInt(circularProgress.dataset.progressValue),
        speed = 40;

    let progress = setInterval(() => {
        progressStartValue++;
        progressValue.textContent = `${progressStartValue}%`;
        circularProgress.style.background = `conic-gradient(#fff ${progressStartValue * 3.6}deg, #000 0deg)`;

        if (progressStartValue === progressEndValue) {
            clearInterval(progress);
        }
    }, speed);
});