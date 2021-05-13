$(document).ready(function() {
    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        $.ajax({
            url: '/cereals?search_filter=' + searchText,
            type: 'GET',
            success: function(resp) {
                var newHtml = resp.data.map(d => {
                    return `<div class="col-md-4 col-md-4-custom">
                            <div class="media">
                                <div class="media-left media-middle">
                                    <img src="${d.firstimage}" class="float-left" />
                                </div>
                                <div class="media-body">
                                    <h1 class="media-heading">${d.name}</h1>
                                    <h4 class="media-heading"> Description</h4>
                                    <p class="media-body">${d.description}</p>
                                    <div class="align-bottom">
                                        <a href="/cereals/${d.id}">
                                            <p>See more</p>
                                        </a>
                                    </div>
                                </div>
                            </div>
                            <div style="text-align: center; display:inline">
                            <button type="button" class="btn" style="color:white; background-color:green; margin:10px; width: 90%;">
                                <span class="glyphicon glyphicon-shopping-cart" aria-hidden="true"></span>Add to cart | &#36;${d.price}
                            </button>

                            </div>
                        </div>`
                });
                $('.cereals').html(newHtml.join(''));
                $('#search-box').val('');
            },
            error: function(xhr, status, error) {
                // TODO: Show toastr
                console.error(error);
            }
        })
    });
});