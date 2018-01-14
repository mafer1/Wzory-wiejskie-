$(document).ready(function onDocumentLoaded() {
});

function openPatternDetailsModal(patternID) {
    jQuery.get("/pattern?pattern_id="+patternID)
        .done(function (data) {
            console.log(data);
           jQuery('#patternModalContent').html(data);
           jQuery('#patternModal').modal()
        });
}