$(document).ready(function() {
    let inputCount = 1;

    // Function to create a new input group
    function createInputGroup(count) {
        return `
            <div class="input-group">
                <input type="text" name="input_${count}" placeholder="Enter value">

                <button type="button" class="add-btn">Add</button>
                <button type="button" class="del-btn">Delete</button>
            </div>`;
    }

    // Add new input group
    $(document).on('click', '.add-btn', function() {
        inputCount++;
        $('#input-container').append(createInputGroup(inputCount));
    });

    // Delete input group
    $(document).on('click', '.del-btn', function() {
        if ($('.input-group').length > 1) {
            $(this).closest('.input-group').remove();
        }
    });
});
