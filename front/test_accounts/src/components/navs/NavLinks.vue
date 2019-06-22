<template>
<ul :id="navid" :class="navclass">
    <li v-for="link in links" :key="link">
        <a :href="link.href">{{ link.name }}</a>
    </li>
</ul>
</template>
