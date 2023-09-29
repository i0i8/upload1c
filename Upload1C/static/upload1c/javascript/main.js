let cls = document.querySelectorAll('tr > td');
for (let i = 0; i < cls.length; i++) {
    if (cls[i].innerText <= '0,0') {
        cls[i].style = 'color: red'
    }
}
if (document.querySelectorAll('td.summ_day_opt').length) {
    let sumDay = document.querySelectorAll('td.summ_day_opt');
    let allSum = 0.0
    for (let i = 0; i < sumDay.length; i++) {
        allSum += parseFloat(sumDay[i].innerHTML.replace(',', '.'))
    }
    let tdInn = document.querySelector('td.result_day_opt');
    tdInn.innerText = allSum.toFixed(2)
}
if (document.querySelectorAll('td.summ_month_opt').length) {
    let sumMonth = document.querySelectorAll('td.summ_month_opt');
    let allSumMonth = 0.0
    for (let i = 0; i < sumMonth.length; i++) {
        allSumMonth += parseFloat(sumMonth[i].innerText.replace(' ', '').replace(',', '.'))
    }
    let tdInn = document.querySelector('td.result_month_opt');
    tdInn.innerText = allSumMonth.toFixed(2)
}
if (document.querySelectorAll('td.summ_year_opt').length) {
    let sumYear = document.querySelectorAll('td.summ_year_opt');
    let allSumYear = 0.0;
    for (let i = 0; i < sumYear.length; i++) {
        allSumYear += parseFloat(sumYear[i].innerText.replace(' ', '').replace(',', '.'))
    }
    let tdInn = document.querySelector('td.result_year_opt');
    tdInn.innerText = allSumYear.toFixed(2)
}

// акординг
let acc = document.getElementsByClassName("accordion");

for (let i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function () {
        this.classList.toggle("active");

        let panel = this.nextElementSibling;
        if (panel.style.display === "block") {
            panel.style.display = "none";
        } else {
            panel.style.display = "block";
        }
    });
}
// 
