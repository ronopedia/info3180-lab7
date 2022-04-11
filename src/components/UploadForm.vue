<template>
    <form @submit.prevent="uploadPhoto" method="post" enctype="multipart/form-data" id="uploadForm" >
    
        <label for="description" class="form-label">Description</label>
        <textarea class="description" id="description" rows="25" required></textarea>
    
        <input type="file" name="photo" id="photo" required>
        <label for="photo">Choose file</label>
        <button v-on:click="uploadPhoto" class="btn btn-primary">Upload File</button>
    
    </form>
</template>

<script> 
export default {
data(){
    return {
        csrf_token: ''
    }
}, 
created() {
    this.getCsrfToken();
},
getCsrfToken() {
    let self = this;
    fetch('/api/csrf-token')
        .then((response) => response.json())
        .then((data) => {
        console.log(data);
        self.csrf_token = data.csrf_token;
    });
},
    
methods: {
    uploadPhoto() {
        let uploadForm = document.getElementById('uploadForm');
        let form_data = new FormData(uploadForm);

        fetch("/api/upload", {
            method: 'POST',
            body: form_data,
            headers: {
                'X-CSRFToken': this.csrf_token
            }
        })
            .then(function (response) {
                return response.json();
            })
            .then(function (data) {
                // display a success message
                console.log(data);
            })
            .catch(function (error) {
                console.log(error);
            });
        }   
    }
}
</script>