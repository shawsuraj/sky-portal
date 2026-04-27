document.addEventListener("DOMContentLoaded", function () {
    const calendarEl = document.getElementById("calendar");
    const openScheduleBtn = document.getElementById("openScheduleBtn");
    const scheduleModalEl = document.getElementById("scheduleModal");
    const meetingDateInput = document.getElementById("meetingDate");

    let scheduleModal = null;

    if (scheduleModalEl) {
        scheduleModal = new bootstrap.Modal(scheduleModalEl);
    }

    // Set minimum date in the date input to today
    if (meetingDateInput) {
        const todayString = new Date().toISOString().split("T")[0];
        meetingDateInput.min = todayString;
    }

    // Checks if selected date is before today
    function isPastDate(dateString) {
        const today = new Date();
        today.setHours(0, 0, 0, 0);

        const selectedDate = new Date(dateString);
        selectedDate.setHours(0, 0, 0, 0);

        return selectedDate < today;
    }

    // Opens the schedule popup/modal
    function openScheduleModal(date = null) {
        if (date) {
            if (isPastDate(date)) {
                alert("You cannot schedule a meeting before today.");
                return;
            }

            if (meetingDateInput) {
                meetingDateInput.value = date;
            }
        }

        if (scheduleModal) {
            scheduleModal.show();
        }
    }

    if (calendarEl) {
        const calendar = new FullCalendar.Calendar(calendarEl, {
            initialView: "dayGridMonth",
            height: 650,
            selectable: true,
            navLinks: false,

            headerToolbar: {
                left: "prev today next",
                center: "title",
                right: "dayGridMonth,timeGridWeek,timeGridDay"
            },

            events: typeof meetingsFromDjango !== "undefined" ? meetingsFromDjango : [],

            // Click calendar date = open popup
            dateClick: function (info) {
                openScheduleModal(info.dateStr);
            }
        });

        calendar.render();
    }

    // Button opens modal without pre-selecting date
    if (openScheduleBtn) {
        openScheduleBtn.addEventListener("click", function () {
            openScheduleModal();
        });
    }

    // When X closes modal, remove backdrop properly
    if (scheduleModalEl) {
        scheduleModalEl.addEventListener("hidden.bs.modal", function () {
            document.querySelectorAll(".modal-backdrop").forEach(function (el) {
                el.remove();
            });

            document.body.classList.remove("modal-open");
            document.body.style.removeProperty("overflow");
            document.body.style.removeProperty("padding-right");
        });
    }
});