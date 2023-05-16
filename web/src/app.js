import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'

import PrimeVue from "primevue/config";
import ToastService from 'primevue/toastservice';
import Button from "primevue/button";
import Card from "primevue/card";
import Carousel from "primevue/carousel";
import Column from "primevue/column";
import DataTable from "primevue/datatable";
import DataView from "primevue/dataview";
import TabMenu from "primevue/tabmenu";
import Textarea from "primevue/textarea";
import Fieldset from "primevue/fieldset";
import Message from "primevue/message";
import Toast from 'primevue/toast';
import InputText from 'primevue/inputtext';
import Slider from 'primevue/slider';
import InputNumber from 'primevue/inputnumber';
import Dropdown from 'primevue/dropdown';
import Calendar from 'primevue/calendar';
import Checkbox from 'primevue/checkbox';
import Password from 'primevue/password';
import Paginator from 'primevue/paginator';
import Dialog from 'primevue/dialog';
import Menubar from 'primevue/menubar';
import ScrollTop from 'primevue/scrolltop';
import ConfirmPopup from 'primevue/confirmpopup';
import FileUpload from 'primevue/fileupload';

import ConfirmationService from 'primevue/confirmationservice';

import "primeflex/primeflex.css";
import "primevue/resources/themes/lara-light-teal/theme.css";
import "primevue/resources/primevue.min.css";
import "primeicons/primeicons.css";
import '@/assets/main.css'


const pinia = createPinia();
const app = createApp(App)
app.use(pinia);
app.use(PrimeVue);
app.use(router);
app.use(ToastService);
app.use(ConfirmationService);

app.component("Button", Button);
app.component("Card", Card);
app.component("Carousel", Carousel);
app.component("Column", Column);
app.component("DataView", DataView);
app.component("DataTable", DataTable);
app.component("TabMenu", TabMenu);
app.component("Textarea", Textarea);
app.component("Fieldset", Fieldset);
app.component("Message", Message);
app.component("Toast", Toast);
app.component("InputText", InputText);
app.component("Slider", Slider);
app.component("InputNumber", InputNumber);
app.component("Dropdown", Dropdown);
app.component("Calendar", Calendar);
app.component("Checkbox", Checkbox);
app.component("Password", Password);
app.component("Paginator", Paginator);
app.component("Dialog", Dialog);
app.component("Menubar", Menubar);
app.component("ScrollTop", ScrollTop);
app.component("ConfirmPopup", ConfirmPopup);
app.component("FileUpload", FileUpload);

export default app;
