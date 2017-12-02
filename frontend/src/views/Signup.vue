<template>
    <div class="container mt-50">
        <h1 class="is-size-2 mb-30 has-text-centered">Signup</h1>
         <vue-form
                    ref="child"
                    :form="form"
                    :type="type"
                    :label="label"
                    :validator="validator"
                    btnValue="Sign Up"
                    @submit="signup"
            ></vue-form>
    </div>
</template>

<script>
    import FormMixin from '../mixins/Form'
    export default {
        mixins: [FormMixin],
        data: () => ({
            form: {
                full_name: '',
                email: '',
                password: '',
                password_confirmation: ''
            },
            label: {
                full_name: 'Full Name',
                email: 'Email',
                password: 'Password',
                password_confirmation: 'Password Confirmation'
            },
            validator: {
                full_name: 'required',
                email: 'required|email',
                password: 'required|min:8|confirmed:password_confirmation',
                password_confirmation: 'required|min:8'
            },
            type: {
                password: 'password',
                password_confirmation: 'password'
            }
        }),
        methods: {
            signup() {
                this.is_valid().then(response => {
                    if (response){
                        console.log(this.form)
                    }
                })
            }
        }
    }
</script>