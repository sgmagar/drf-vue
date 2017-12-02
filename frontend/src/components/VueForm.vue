<template>
    <div>
        <div v-if="formError" class="has-text-danger">
            {{ formError }}
        </div>
        <form ref="form" @submit.prevent="$emit('submit')">
            <div v-for="(value, key) in form" class="field">
                <label class="label">{{ label[key] }}</label>
                <div>
                    <textarea v-if="is_textarea(key)"
                              :class="[errors.collect(key).length?'is-danger':'', 'textarea']"
                              v-model="form[key]"
                              :placeholder="label[key]"
                              :name="key"
                              v-validate="validator[key]"

                    >
                    </textarea>
                    <div v-else-if="is_select(key)" class="select">
                        <select
                                :class="errors.collect(key).length?'is-danger':''"
                                v-model="form[key]"
                                :placeholder="label[key]"
                                :name="key"
                                v-validate="validator[key]">
                            <option value="" disabled selected>{{ label[key] }}</option>
                            <option v-for="option in option[key]" :value="option">{{ option }}</option>
                        </select>
                    </div>
                    <input v-else
                           :class="[errors.collect(key).length?'is-danger':'' , 'input']"
                           v-model="form[key]"
                           :type="type_exists(key)?type[key] : 'text'"
                           :placeholder="label[key]"
                           :name="key"
                           v-validate="validator[key]"
                    >
                    <span v-if="errors.collect(key).length">
                        <div
                                class="has-text-danger"
                                v-for="error in errors.collect(key)"
                        >
                            {{error}}
                        </div>
                    </span>
                </div>
            </div>
            <input type="submit" class="button is-primary" :value="btnValue">
        </form>
    </div>
</template>

<script>
    export default {
        props: ['form', 'label', 'validator', 'type', 'option', 'btnValue'],
        data: () => ({
            formError: ''
        }),
        $validates: true,
        computed: {},
        methods: {
            is_textarea(key) {
                return this.type && (this.type[key] === 'textarea')
            },
            is_select(key) {
                return this.type && (this.type[key] === 'select')
            },
            type_exists(key){
                return this.type && this.type[key]
            }
        },
    }
</script>