<template>
  <div class="flex justify-between items-center mb-4">
    <input
      v-model="title"
      class="basis-3/4 border-0 bg-white text-3xl font-normal focus:outline-0"
      placeholder="Untitled Document" />
    <div>
      <Button
        class="flex-none mr-1"
        appearance="primary"
        @click="
          $resources.createDocument.submit({
            title: title,
            content: content,
            parent: currentFolderID,
          })
        ">
        Save
      </Button>
      <Button @click="$router.go(-1)">Discard</Button>
    </div>
  </div>
  <TextEditor
    id="editorElem"
    v-model="content"
    editor-class="border max-w-none rounded-b-lg p-3 overflow-auto focus:outline-none"
    :fixed-menu="true" />
</template>

<!--  
  State testing 
  <div class="content">
    <h3>Content</h3>
      {{ content }}
  </div> 
-->

<script>
import { Button } from "frappe-ui";
import TextEditor from "@/components/DocEditor/TextEditor.vue";
import { computed } from "@vue/reactivity";

export default {
  components: {
    TextEditor,
    Button,
  },
  emits: ["uploadFile"],
  data() {
    return {
      title: null,
      content: null,
    };
  },
  computed: {
    currentFolderID() {
      return this.$store.state.currentFolderID;
    },
  },
  resources: {
    createDocument() {
      return {
        url: "drive.api.documents.create_document",
        params: {
          title: this.title,
          content: this.content,
          parent: "",
        },
        onSuccess(data) {
          console.log(data);
        },
        onError(data) {
          console.log(data);
        },
        auto: false,
      };
    },
  },
};
</script>

<style lang="scss">
/* Basic editor styles */
.ProseMirror {
  > * + * {
    margin-top: 0.75em;
  }

  code {
    background-color: rgba(#616161, 0.1);
    color: #616161;
  }
}

.content {
  padding: 1rem 0 0;

  h3 {
    margin: 1rem 0 0.5rem;
  }

  pre {
    border-radius: 5px;
    color: #333;
  }

  code {
    display: block;
    white-space: pre-wrap;
    font-size: 0.8rem;
    padding: 0.75rem 1rem;
    background-color: #e9ecef;
    color: #495057;
  }
}
</style>
