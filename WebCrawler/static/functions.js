function runScraper() {
    // Sends a GET request to 'run_scraper' endpoint
    $.get('run_scraper', function() {
        // Callback function executed upon successful response
        reloadTable();
    });
}

function getOnlyMoreThanFiveWords() {
    // Sends a GET request to 'get_more_than_five_words' endpoint
    $.get('get_more_than_five_words', function() {
        // Callback function executed upon successful response
        reloadTable();
    });
}

function getOnlyLessThanFiveWords() {
    // Sends a GET request to 'get_less_than_five_words' endpoint
    $.get('get_less_than_five_words', function() {
        // Callback function executed upon successful response
        reloadTable();
    });
}

function reloadTable() {
    // Reloads the content of the '#news-table' element to update de entries
    $('#news-table').load(window.location.href + ' #news-table');
}