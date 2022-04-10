<template>
<form @submit.prevent="uploadPhoto" id="uploadForm" class="d-flex flex-column justify-content-center">
    <div>
        <label for="description" class="form-label">Description</label>
        <textarea class="form-control" id="desc" rows="3"></textarea>
    </div>
    <div>
        <input type="file" id="formFileSm" class="form-control form-control-sm" >
        <label for="formFileSm" class="form-label">Choose file</label>
        <button v-on:click="uploadPhoto" class="btn btn-primary">Upload File</button>
    </div>
</form>
</template>

<script> 
export default {
data(){
    return {
        csrf_token: ''
    }
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
    created() {
        this.getCsrfToken();
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