import VueForm from '../components/VueForm.vue'

export default {
    components: {VueForm},
    data: () => ({}),
    methods: {
        is_valid (ref='') {
            return new Promise((resolve, reject) => {
                if (!ref) {
                    this.$refs.child.$validator.validateAll().then(response => {
                        resolve(response)
                    })
                } else{
                    this.$refs[ref].$validator.validateAll().then(response => {
                        resolve(response)
                    })
                }
            })
        },
        clear (ref='') {
            if (!ref) {
                this.$refs.child.$validator.reset()
                this.$refs.child.$refs.form.reset()
                this.set_form_error(null, '')
            } else {
                this.$refs[ref].$validator.reset()
                this.$refs[ref].$refs.form.reset()
                this.set_form_error(ref, '')
            }

        },
        set_field_errors (errors, ref='') {
            if (!ref) {
                this.$refs.child.errors.items[0] = errors
            } else {
                this.$refs[ref].errors.items[0] = errors
            }
        },
        set_form_error (error, ref='') {
            if (!ref) {
                this.$refs.child.formError = error
            } else {
                this.$refs[ref].formError = error
            }
        }
    }
}