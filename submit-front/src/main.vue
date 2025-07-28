<script setup lang="ts">
// imports
import { ref, onMounted } from "vue";
import { marked } from "marked";

// values
const markdownText = ref("");
const password = ref("");
const markdownHTML = ref();
const title = ref("");
const requestFailed = ref(false);
const previewContent = () => {
    console.log(markdownText);
    markdownHTML.value = marked.parse(markdownText.value);
};

const submitContent = async () => {
    requestFailed.value = false;

    if (!markdownText || !password || !title) {
        requestFailed.value = true;
    }
    const req = await fetch("/api/submit", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            markdownText: markdownText,
            authKey: password,
            title: title,
        }),
    });
    if (!req.ok) {
        requestFailed.value = true;
        return;
    }
    const res = await req.json();
    if (!res.success) {
        requestFailed.value = true;
        return;
    }
    localStorage.removeItem("lastSavedMarkdownData");
};

onMounted(() => {
    const lastSavedMarkdownData = localStorage.getItem("lastSavedMarkdownData");
    if (lastSavedMarkdownData) {
        markdownText.value = lastSavedMarkdownData;
    }
});
</script>
<template>
    <div class="flex flex-col">
        <span v-if="requestFailed" style="color: red"
            >Your request failed!</span
        >
        <span>Enter your creds</span>
        <input type="password" v-model="password" class="border" />
        <span>Title</span>
        <input type="text" v-model="title" class="border" />
        <span>Input your content in Markdown!</span>
        <div class="border">
            <textarea v-model="markdownText" class="markdowntext" />
        </div>
        <div class="flex flex-row">
            <button @click="previewContent" class="button">
                Preview Content?
            </button>
            <button @click="submitContent" class="button">
                Submit Content
            </button>
        </div>
        <span>Preview</span>
        <div v-html="markdownHTML"></div>
    </div>
</template>

<style>
.flex {
    display: flex;
}
.flex-col {
    flex-direction: column;
}
.markdowntext {
    height: 70vh;
    width: 75%;
    margin: 20px;
}
.flex-row {
    flex-direction: row;
}
</style>
