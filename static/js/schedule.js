document.addEventListener('DOMContentLoaded', function () {

    // get main page elements
    var calendarEl = document.getElementById('calendar');
    var form = document.getElementById('meetingForm');
    var upcoming = document.getElementById('upcomingMeetings');
    var openButton = document.getElementById('openScheduleBtn');
    var noMeetingsText = document.getElementById('noMeetingsText');

    // get form inputs
    var titleInput = document.getElementById('meetingTitle');
    var dateInput = document.getElementById('meetingDate');
    var timeInput = document.getElementById('meetingTime');
    var teamInput = document.getElementById('meetingTeam');
    var locationInput = document.getElementById('meetingLocation');
    var messageInput = document.getElementById('meetingMessage');

    // create bootstrap modal
    var modal = new bootstrap.Modal(document.getElementById('scheduleModal'));

    // store temporary meetings only for this page load
    var temporaryMeetings = [];
    var meetingCounter = 0;

    // set minimum date to today so older dates cannot be selected
    var today = new Date();
    var todayString = today.toISOString().split('T')[0];
    dateInput.min = todayString;

    // open modal and optionally fill selected date
    function openModal(selectedDate = '') {
        form.reset();
        dateInput.min = todayString;

        if (selectedDate) {
            dateInput.value = selectedDate;
        }

        modal.show();
    }

    // hide/show "No meetings yet"
    function updateNoMeetingsText() {
        if (upcoming.querySelectorAll('.meeting-card').length > 0) {
            noMeetingsText.style.display = 'none';
        } else {
            noMeetingsText.style.display = 'block';
        }
    }

    // add meeting card to upcoming panel
    function addMeetingToUI(meeting) {
        upcoming.insertAdjacentHTML('beforeend', `
            <div class="card mb-2 p-2 meeting-card" data-id="${meeting.id}">
                <strong>${meeting.title}</strong><br>
                Date: ${meeting.date}<br>
                Time: ${meeting.time}<br>
                Team: ${meeting.team}<br>
                Location: ${meeting.location}<br>
                Message: ${meeting.message || 'No message'}<br>

                <button class="btn btn-danger btn-sm mt-2 remove-btn">
                    Remove
                </button>
            </div>
        `);

        updateNoMeetingsText();
    }

    // create calendar
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',

        headerToolbar: {
            left: 'prev,today,next',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,timeGridDay'
        },

        // empty for testing right now
        events: meetingsFromDjango,

        // clicking a date opens the popup
        dateClick: function (info) {
            // do not allow clicking older dates
            if (info.dateStr < todayString) {
                alert('You cannot create a meeting before today.');
                return;
            }

            openModal(info.dateStr);
        }
    });

    // render calendar
    calendar.render();

    // open popup from button
    openButton.addEventListener('click', function () {
        openModal();
    });

    // handle form submit
    form.addEventListener('submit', function (e) {
        e.preventDefault();

        // stop old dates from being submitted
        if (dateInput.value < todayString) {
            alert('You cannot create a meeting before today.');
            return;
        }

        // create temporary meeting object
        var meeting = {
            id: 'meeting-' + meetingCounter,
            title: titleInput.value,
            date: dateInput.value,
            time: timeInput.value,
            team: teamInput.value,
            location: locationInput.value,
            message: messageInput.value,
            dateTime: dateInput.value + 'T' + timeInput.value
        };

        meetingCounter++;
        temporaryMeetings.push(meeting);

        // add event to calendar
        calendar.addEvent({
            id: meeting.id,
            title: meeting.title,
            start: meeting.dateTime
        });

        // add meeting card to upcoming list
        addMeetingToUI(meeting);

        // close popup after confirm
        modal.hide();

        // reset form after closing
        form.reset();
    });

    // remove button logic
    upcoming.addEventListener('click', function (e) {
        if (e.target.classList.contains('remove-btn')) {
            var card = e.target.closest('.meeting-card');
            var meetingId = card.getAttribute('data-id');

            // remove from upcoming panel
            card.remove();

            // remove from calendar
            var event = calendar.getEventById(meetingId);
            if (event) {
                event.remove();
            }

            // remove from temporary array
            temporaryMeetings = temporaryMeetings.filter(function (meeting) {
                return meeting.id !== meetingId;
            });

            updateNoMeetingsText();
        }
    });

    // run once on page load
    updateNoMeetingsText();
});