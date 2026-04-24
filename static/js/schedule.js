document.addEventListener("DOMContentLoaded", function () {
    const calendarEl = document.getElementById("calendar");
    const openScheduleBtn = document.getElementById("openScheduleBtn");
    const scheduleModalEl = document.getElementById("scheduleModal");

    if (calendarEl) {
        const calendar = new FullCalendar.Calendar(calendarEl, {
            initialView: "dayGridMonth",
            height: 650,
            headerToolbar: {
                left: "prev today next",
                center: "title",
                right: "dayGridMonth,timeGridWeek,timeGridDay"
            },
            events: typeof meetingsFromDjango !== "undefined" ? meetingsFromDjango : []
        });

        calendar.render();
    }

    if (openScheduleBtn && scheduleModalEl) {
        openScheduleBtn.addEventListener("click", function () {
            const modal = new bootstrap.Modal(scheduleModalEl);
            modal.show();
        });
    }
});