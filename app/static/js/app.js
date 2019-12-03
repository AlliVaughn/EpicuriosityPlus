var vizTrends;
var vizNutritionalVs;
var currentNutritionalVsFilterName = 'All';


// wire up javascript to menus
$(document).ready(function () {
    // Jquery for the trend list group
    $('.list-group-item').on('click', function () {
        // console.log('here!');
        var $this = $(this);
        var $alias = $this.data('alias');

        $('.list-group > .list-group-item').removeClass('active');
        $this.toggleClass('active');

        // console.log($this.text())
        // Pass clicked link element to another function
        switchTrend($this, $alias);
    });


    $("#nutritionalButtons :input").change(function () {
        // console.log(this); // points to the clicked input button
        var $this = $(this);
        var $alias = $this.data('alias');
        // console.log($alias);

        switchNutritionalView($alias);
    });
});

function switchTrend($this, trendSheetName) {
    // console.log($this.text());  // Will log Paris | France | etc...
    // console.log('in switch trend')
    // console.log(trendWorkbookName);  // Will output whatever is in data-alias=""

    const trendName = $this.text();
    var workbook;

    // change area chart worksheet
    workbook = vizTrends.getWorkbook();
    // console.log(trendsWorkbook);
    workbook.activateSheetAsync(trendSheetName);

};

function switchNutritionalView(sheetName) {
    console.log('in nutritional change');
    // console.log($alias);

    var workbook = vizNutritionalVs.getWorkbook();
    console.log(workbook)
    // console.log(nutritionalVsWorkbook);
    workbook.activateSheetAsync(sheetName);

    console.log('after sheet change')
    // console.log($this.text().trim());  // Will log Paris | France | etc...

    // console.log($alias);  // Will output whatever is in data-alias=""
};


//load the tableau viz's
window.onload = function () {
    //load the viz
    var vizTrendsDiv = document.getElementById('vizTrends');
    var vizNutritionalVsDiv = document.getElementById('vizNutritionalVs');

    var vizTrendsURL = 'https://public.tableau.com/views/Epicuriosity-Top10TrendTags/Top10TrendTags?:display_count=y&:origin=viz_share_link';
    var vizNutritionalVsURL = 'https://public.tableau.com/views/Epicuriousity-NutritionScatter/CaloriesvsFat?:display_count=y&publish=yes&:origin=viz_share_link';

    var trendOptions = {
        width: '1150px',
        height: '600px',
        hideToolbar: true,
        hideTabs: true
    };

    var nutritionalVsOptions = {
        width: '700px',
        height: '600px',
        hideToolbar: true,
        hideTabs: true
    };

    vizTrends = new tableau.Viz(vizTrendsDiv, vizTrendsURL, trendOptions);
    vizNutritionalVs = new tableau.Viz(vizNutritionalVsDiv, vizNutritionalVsURL, nutritionalVsOptions);

    //draw word cloud
    // drawWordCloud(text_string);
};