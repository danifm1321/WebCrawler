function runScraper() {
    $.get('run_scraper', function(data) {
        reloadTable();
    });
}

function getOnlyMoreThanFiveWords() {
    $.get('get_more_than_five_words', function(data) {
        reloadTable();
    });
}

function getOnlyLessThanFiveWords() {
    $.get('get_less_than_five_words', function(data) {
        reloadTable();
    });
}

function reloadTable() {
    $('#news-table').load(window.location.href + ' #news-table');
}