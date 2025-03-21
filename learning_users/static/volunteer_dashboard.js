

async function loadPatients() {
    try {
        const response = await fetch('/api/patients/');
        const patients = await response.json();

        const table = document.getElementById("patients-list");
        table.innerHTML = "";  // Изчистваме старите записи

        patients.forEach(patient => {
            let row = `<tr>
                <td>${patient.user__first_name} ${patient.user__last_name}</td>
                <td>${patient.needs}</td>
                <td>${patient.location}</td>
            </tr>`;
            table.innerHTML += row;
        });
    } catch (error) {
        console.error("Грешка при зареждане на пациенти:", error);
    }
}

// Автоматично зареждане на пациенти при зареждане на страницата
window.onload = loadPatients;

