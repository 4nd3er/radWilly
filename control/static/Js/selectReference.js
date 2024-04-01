const selectFilter = document.getElementById('selectFilter');
const brandSearch = document.getElementById('brandSearch');
const placeSearch = document.getElementById('placeSearch');

selectFilter.addEventListener('input', function (e) {
    if (e.target.value === 'brand') {
    }
    switch (e.target.value) {
        case 'brand':
            brandSearch.style.display = 'flex';
            setTimeout(() => {
                brandSearch.style.opacity = '1';
            }, 100);
            placeSearch.style.display = 'none';
            placeSearch.style.opacity = '0';
            break;
        case 'place':
            placeSearch.style.display = 'flex';
            setTimeout(() => {
                placeSearch.style.opacity = '1';
            }, 100);
            brandSearch.style.display = 'none';
            brandSearch.style.opacity = '0';
            break;
        default:
            brandSearch.style.opacity = '0';
            setTimeout(() => {
                brandSearch.style.display = 'none';
                placeSearch.style.display = 'none';
            }, 500);
            placeSearch.style.opacity = '0';
            break;
    }
})