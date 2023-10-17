let cls = document.querySelectorAll('tr > td');
for (let i = 0; i < cls.length; i++) {
    if (cls[i].innerText < '0,0') {
        cls[i].style = 'color: red'
    }
}
//говнокод :)
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
if (document.querySelectorAll('td.summ_day_ret').length) {
    let sumDayRet = document.querySelectorAll('td.summ_day_ret');
    let allSumDayRet = 0.0;
    for (let i = 0; i < sumDayRet.length; i++) {
        allSumDayRet += parseFloat(sumDayRet[i].innerText.replace(' ', '').replace(',', '.'))
    }
    let tdInn = document.querySelector('td.result_day_ret');
    tdInn.innerText = allSumDayRet.toFixed(2)
}
if (document.querySelectorAll('td.summ_month_ret').length) {
    let sumMonthRet = document.querySelectorAll('td.summ_month_ret');
    let allSumMonthRet = 0.0;
    for (let i = 0; i < sumMonthRet.length; i++) {
        allSumMonthRet += parseFloat(sumMonthRet[i].innerText.replace(' ', '').replace(',', '.'))
    }
    let tdInn = document.querySelector('td.result_month_ret');
    tdInn.innerText = allSumMonthRet.toFixed(2)
}
if (document.querySelectorAll('td.summ_year_ret').length) {
    let sumYearRet = document.querySelectorAll('td.summ_year_ret');
    let allSumYearRet = 0.0;
    for (let i = 0; i < sumYearRet.length; i++) {
        allSumYearRet += parseFloat(sumYearRet[i].innerText.replace(' ', '').replace(',', '.'))
    }
    let tdInn = document.querySelector('td.result_year_ret');
    tdInn.innerText = allSumYearRet.toFixed(2)
}
if (document.querySelectorAll('td.result_day_all').length) {
    let sumDayOpt = document.querySelector('td.result_day_opt').innerText;
    let sumDayRet = document.querySelector('td.result_day_ret').innerText;
    let sumMonthOpt = document.querySelector('td.result_month_opt').innerText;
    let sumMonthRet = document.querySelector('td.result_month_ret').innerText;
    let sumYearOpt = document.querySelector('td.result_year_opt').innerText;
    let sumyearRet = document.querySelector('td.result_year_ret').innerText;
    let dayResult = parseFloat(sumDayOpt) + parseFloat(sumDayRet);
    let monthResult = parseFloat(sumMonthOpt) + parseFloat(sumMonthRet);
    let yearResult = parseFloat(sumYearOpt) + parseFloat(sumyearRet);
    let tdInnDay = document.querySelector('td.result_day_all');
    let tdInnMonth = document.querySelector('td.result_month_all');
    let tdInnYear = document.querySelector('td.result_year_all');
    tdInnDay.innerText = dayResult;
    tdInnMonth.innerText = monthResult;
    tdInnYear.innerText = yearResult;
}
// retail
if (document.querySelectorAll('td.ret_allDay').length) {
    let retDay = document.querySelectorAll('td.ret_day');
    let allSummRetDay = 0.0;
    for (let i = 0; i < retDay.length; i++) {
        allSummRetDay += parseFloat(retDay[i].innerText.replace(' ', '').replace(',', '.'))
    }
    let tdInn = document.querySelector('td.ret_allDay');
    tdInn.innerText = allSummRetDay.toFixed(2)
}
if (document.querySelectorAll('td.ret_allDay').length) {
    let retPlanMonth = document.querySelectorAll('td.ret_planMonth');
    let allSummRetPlanMonth = 0.0;
    for (let i = 0; i < retPlanMonth.length; i++) {
        allSummRetPlanMonth += parseFloat(retPlanMonth[i].innerText.replace(' ', '').replace(',', '.'))
    }
    let tdInn = document.querySelector('td.ret_allPlanMonth');
    tdInn.innerText = allSummRetPlanMonth.toFixed(2)
}
if (document.querySelectorAll('td.ret_allDay').length) {
    let retFactMonth = document.querySelectorAll('td.ret_factMonth');
    let allSummRetFactMonth = 0.0;
    for (let i = 0; i < retFactMonth.length; i++) {
        allSummRetFactMonth += parseFloat(retFactMonth[i].innerText.replace(' ', '').replace(',', '.'))
    }
    let tdInn = document.querySelector('td.ret_allFactMont');
    tdInn.innerText = allSummRetFactMonth.toFixed(2)
}
if (document.querySelectorAll('td.ret_allDay').length) {
    let retPlan = document.querySelectorAll('td.ret_planMonth')
    let retFact = document.querySelectorAll('td.ret_factMonth')
    let tdInn = document.querySelectorAll('td.ret_deviations');
    let retDeviations = 0.0
    for (let i = 0; i < retPlan.length; i++) {
        retDeviations = parseFloat(retFact[i].innerText.replace(' ', '').replace(',', '.') - parseFloat(retPlan[i].innerText.replace(' ', '').replace(',', '.')))
        tdInn[i].innerText = retDeviations.toFixed(2)
    }
}
if (document.querySelectorAll('td.ret_allDay').length) {
    let retDeviations = document.querySelectorAll('td.ret_deviations');
    let allSummRetDeviations = 0.0;
    for (let i = 0; i < retDeviations.length; i++) {
        allSummRetDeviations += parseFloat(retDeviations[i].innerText.replace(' ', '').replace(',', '.'))
    }
    let tdInn = document.querySelector('td.ret_allDeviations');
    tdInn.innerText = allSummRetDeviations.toFixed(2)
}
// end retail
// opt
if (document.querySelectorAll('td.opt_allDay').length) {
    let optDay = document.querySelectorAll('td.opt_day');
    let allSummOptDay = 0.0;
    for (let i = 0; i < optDay.length; i++) {
        allSummOptDay += parseFloat(optDay[i].innerText.replace(' ', '').replace(',', '.'))
    }
    let tdInn = document.querySelector('td.opt_allDay');
    tdInn.innerText = allSummOptDay.toFixed(2)
}
if (document.querySelectorAll('td.opt_allDay').length) {
    let optPlanMonth = document.querySelectorAll('td.opt_planMonth');
    let allSummOptPlanMonth = 0.0;
    for (let i = 0; i < optPlanMonth.length; i++) {
        allSummOptPlanMonth += parseFloat(optPlanMonth[i].innerText.replace(' ', '').replace(',', '.'))
    }
    let tdInn = document.querySelector('td.opt_allPlanMonth');
    tdInn.innerText = allSummOptPlanMonth.toFixed(2)
}
if (document.querySelectorAll('td.opt_allDay').length) {
    let optFactMonth = document.querySelectorAll('td.opt_factMonth');
    let allSummOptFactMonth = 0.0;
    for (let i = 0; i < optFactMonth.length; i++) {
        allSummOptFactMonth += parseFloat(optFactMonth[i].innerText.replace(' ', '').replace(',', '.'))
    }
    let tdInn = document.querySelector('td.opt_allFactMonth');
    tdInn.innerText = allSummOptFactMonth.toFixed(2)
}
if (document.querySelectorAll('td.opt_allDay').length) {
    let optPlan = document.querySelectorAll('td.opt_planMonth')
    let optFact = document.querySelectorAll('td.opt_factMonth')
    let tdInn = document.querySelectorAll('td.opt_deviations');
    let optDeviations = 0.0
    for (let i = 0; i < optPlan.length; i++) {
        optDeviations = parseFloat(optFact[i].innerText.replace(' ', '').replace(',', '.') - parseFloat(optPlan[i].innerText.replace(' ', '').replace(',', '.')))
        tdInn[i].innerText = optDeviations.toFixed(2)
    }
}
if (document.querySelectorAll('td.opt_allDay').length) {
    let optDeviations = document.querySelectorAll('td.opt_deviations');
    let allDeviations = 0.0;
    for (let i = 0; i < optDeviations.length; i++) {
        allDeviations += parseFloat(optDeviations[i].innerText.replace(' ', '').replace(',', '.'))
    }
    let tdInn = document.querySelector('td.opt_allDeviations');
    tdInn.innerText = allDeviations.toFixed(2)
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
