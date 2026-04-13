document.addEventListener('DOMContentLoaded', function () {

    // get main elements from the page
    var calendarEl = document.getElementById('calendar');
    var form = document.getElementById('meetingForm');
    var openButton = document.getElementById('openScheduleBtn');
    var dateInput = document.getElementById('meetingDate');

    // create bootstrap modal
    var modal = new bootstrap.Modal(document.getElementById('scheduleModal'));

    // get today's date in YYYY-MM-DD format
    var today = new Date().toISOString().split('T')[0];

    // stop user picking past dates in the form
    dateInput.min = today;

    // open modal and optionally fill selected date
    function openModal(selectedDate = '') {
        form.reset();
        dateInput.min = today;

        if (selectedDate) {
            if (selectedDate < today) {
                alert('You cannot create a meeting before today.');
                return;
            }
            dateInput.value = selectedDate;
        }

        modal.show();
    }

    // create FullCalendar
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',

        headerToolbar: {
            left: 'prev,today,next',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,timeGridDay'
        },

        // meetings already saved in the database
        events: meetingsFromDjango,

        // open modal when a calendar date is clicked
        dateClick: function (info) {
            openModal(info.dateStr);
        }
    });

    // render calendar
    calendar.render();

    // open popup when the button under the calendar is clicked
    openButton.addEventListener('click', function () {
        openModal();
    });

    // stop form submit if the date is before today
    form.addEventListener('submit', function (e) {
        if (dateInput.value < today) {
            e.preventDefault();
            alert('You cannot create a meeting before today.');
        }
    });

});