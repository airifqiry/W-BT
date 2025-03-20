function daysInMonth(month, year) {
    return new Date(year, month + 1, 0).getDate();
}

function updateCalendar() {
    const calendar = document.getElementById("calendar");
    calendar.innerHTML = "";
    const month = parseInt(document.getElementById("month").value);
    const year = parseInt(document.getElementById("year").value);
    const days = daysInMonth(month, year);
    
    const daysOfWeek = ["Понеделник", "Вторник", "Сряда", "Четвъртък", "Петък", "Събота", "Неделя"];
    
    const table = document.createElement("table");
    table.classList.add("calendar-table");
    
    const headerRow = document.createElement("tr");
    daysOfWeek.forEach(day => {
        const headerCell = document.createElement("th");
        headerCell.textContent = day;
        headerRow.appendChild(headerCell);
    });
    table.appendChild(headerRow);
    
    let date = 1;
    for (let row = 0; row < 6; row++) {
        const tableRow = document.createElement("tr");
        for (let col = 0; col < 7; col++) {
            const cell = document.createElement("td");
            if ((row === 0 && col < new Date(year, month, 1).getDay() - 1) || date > days) {
                cell.textContent = "";
            } else {
                cell.textContent = date;
                cell.classList.add("day");
                cell.onclick = () => addEvent(cell);
                date++;
            }
            tableRow.appendChild(cell);
        }
        table.appendChild(tableRow);
    }
    calendar.appendChild(table);
}

function addEvent(day) {
    const eventText = prompt("Въведи подробности за събитието:");
    if (eventText) {
        const eventDiv = document.createElement("div");
        eventDiv.classList.add("event");
        eventDiv.textContent = eventText;
        day.appendChild(eventDiv);
    }
}

updateCalendar();