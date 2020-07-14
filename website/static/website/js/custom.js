document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.fixed-action-btn');
    var instances = M.FloatingActionButton.init(elems, options);
});

// Or with jQuery

$(document).ready(function(){
    $('.fixed-action-btn').floatingActionButton();
    $('.fixed-action-btn.top').floatingActionButton({
        direction: 'top'
    });
    $('.fixed-action-btn.click-to-toggle').floatingActionButton({
        direction: 'top',
        hoverEnabled: false
    });
});
var snapSlider = document.getElementById('slider-snap');

noUiSlider.create(snapSlider, {
    start: [0, 90000000],
    snap: false,
    connect: true,
    step: 25000,
    range: {
        'min': 0,
        'max': 100000000
    }
});
var snapValues = [
    document.getElementById('slider-snap-value-lower'),
    document.getElementById('slider-snap-value-upper')
];
var inputValues = [
    document.getElementById('slider-snap-input-lower'),
    document.getElementById('slider-snap-input-upper')
];
snapSlider.noUiSlider.on('update', function (values, handle) {
    snapValues[handle].innerHTML = Number(values[handle]).toLocaleString('pt-BR');
});

snapSlider.noUiSlider.on('change', function (values, handle) {
    inputValues[handle].value = values[handle];
});
