// Wait until the page is fully loaded before running any JS
document.addEventListener("DOMContentLoaded", function () {

    // Get important elements from the page
    const calendarEl = document.getElementById("calendar"); // calendar container
    const openScheduleBtn = document.getElementById("openScheduleBtn"); // button to open modal
    const scheduleModalEl = document.getElementById("scheduleModal"); // modal element
    const meetingDateInput = document.getElementById("meetingDate"); // date input inside modal

    let scheduleModal = null;

    // Initialise Bootstrap modal if it exists
    if (scheduleModalEl) {
        scheduleModal = new bootstrap.Modal(scheduleModalEl);
    }

    // Set minimum date in the input field to today (prevents past selection)
    if (meetingDateInput) {
        const todayString = new Date().toISOString().split("T")[0];
        meetingDateInput.min = todayString;
    }

    // Function to check if selected date is before today
    function isPastDate(dateString) {
        const today = new Date();
        today.setHours(0, 0, 0, 0); // reset time

        const selectedDate = new Date(dateString);
        selectedDate.setHours(0, 0, 0, 0); // reset time

        return selectedDate < today; // true if date is in the past
    }

    // Function to open the schedule modal
    function openScheduleModal(date = null) {

        // If a date is passed (clicked from calendar)
        if (date) {

            // Prevent selecting past dates
            if (isPastDate(date)) {
                alert("You cannot schedule a meeting before today.");
                return;
            }

            // Pre-fill the date input with selected date
            if (meetingDateInput) {
                meetingDateInput.value = date;
            }
        }

        // Show the modal
        if (scheduleModal) {
            scheduleModal.show();
        }
    }

    // Initialise FullCalendar if calendar exists
    if (calendarEl) {
        const calendar = new FullCalendar.Calendar(calendarEl, {
            initialView: "dayGridMonth", // default view
            height: 650,
            selectable: true,
            navLinks: false,

            // Calendar header controls
            headerToolbar: {
                left: "prev today next",
                center: "title",
                right: "dayGridMonth,timeGridWeek,timeGridDay"
            },

            // Load events from Django (if available)
            events: typeof meetingsFromDjango !== "undefined" ? meetingsFromDjango : [],

            // When a date is clicked → open modal
            dateClick: function (info) {
                openScheduleModal(info.dateStr);
            }
        });

        // Render the calendar
        calendar.render();
    }

    // Button click → open modal (no pre-selected date)
    if (openScheduleBtn) {
        openScheduleBtn.addEventListener("click", function () {
            openScheduleModal();
        });
    }

    // Fix modal closing issue (removes leftover backdrop)
    if (scheduleModalEl) {
        scheduleModalEl.addEventListener("hidden.bs.modal", function () {

            // Remove all modal backdrops manually
            document.querySelectorAll(".modal-backdrop").forEach(function (el) {
                el.remove();
            });

            // Reset body styles (fix scroll issues)
            document.body.classList.remove("modal-open");
            document.body.style.removeProperty("overflow");
            document.body.style.removeProperty("padding-right");
        });
    }
});