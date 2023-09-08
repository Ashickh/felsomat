$(document).ready(function () {
    // Handle form submission using AJAX
    $('#groups-form').on('submit', function (e) {
        e.preventDefault(); // Prevent the default form submission


        var createComponentUrl = "{% url 'create-groups' %}";
        var form = this;

        $.ajax({
            url: createComponentUrl,  // Use the generated URL
            method: 'POST',
            data: $(this).serialize(),  // Serialize form data
            success: function (data) {
                // Update the table with the newly created component
                $('#groups-table').append('<tr><td>' + data.project + '</td><td>' 
                + data.item_name + '</td> <td>' + data.base_quantity + '</td> <td>' 
                    + data.group_cost + '</td> <td>' + data.type + '</td></tr>');

                $(form)[0].reset();
            },
            error: function (error) {
                console.error('Error:', error);
            }
        });
    });
});