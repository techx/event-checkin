$(document).ready(function() {
    var readyToSubmit = false;
    var timeout = false;
    var currentRequest = 0;

    var setMessage = function(message) {
        $('.default').hide();
        $('.found').hide();
        $('#info-container').text(message);
        $(".default").show();
    }

    $('#main-form').submit(function() {
        console.log(readyToSubmit);
        return readyToSubmit;
    });

    $('#kerberos').on('change keyup paste', function(e) {
        if (e.which === undefined) return;
        if (e.which == 13) {
            $('#main-form').submit();
            return;
        };
        readyToSubmit = false;
        if (timeout !== false) {
            clearTimeout(timeout);
        }
        timeout = setTimeout(function() {
            currentRequest += 1;
            var thisRequest = currentRequest;
            setMessage("Loading...");
            $.get('/lookup', { kerberos: $('#kerberos').val() }).done(function(result) {
                if (currentRequest != thisRequest) return;
                $('.default').hide();
                $('.found').hide();

                $('#name').val(result.name);
                $('#major').val(result.major);

                $('.found').show();
                readyToSubmit = true;
            }).fail(function(x) {
                if (currentRequest != thisRequest) return;
                if (x.status == 404) {
                    setMessage("We could not find a user with that kerberos.");
                } else {
                    setMessage("There was an internal error.");
                }
            });

            timeout = false;
        }, 150);
    });

    $('#name').on('change keyup paste', function(e) { if (e.which == 13) { $('#main-form').submit(); }; });
    $('#major').on('change keyup paste', function(e) { if (e.which == 13) { $('#main-form').submit(); }; });
});