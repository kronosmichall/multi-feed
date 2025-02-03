<script lang="ts">
  let {
    id,
    creator,
    tags,
    title
  } = $props();

  function videoUrl() {
    return `https://www.tiktok.com/${creator}/video/${id}`
  }

  function creatorUrl() {
    return `https://www.tiktok.com/${creator}?refer=embed`
  }

  function tagUrl(tag) {
    return `https://www.tiktok.com/tags/${tag}?refer=embed`
  }
  
</script>
<blockquote class="tiktok-embed" cite={videoUrl()} data-video-id="{id}" style="max-width: 605px;min-width: 325px;" > 
  <section> 
    <a target="_blank" title="@szybki.adder" href={creatorUrl()}>{creator}</a>
    {title}
    {#each tags as tag}
      <a title={tag} target="_blank" href=tagUrl(tag)>#{tag}</a>
    {/each}
    <a target="_blank" title="♬ dźwięk oryginalny - ig: szybki.adder" href="https://www.tiktok.com/music/dźwięk-oryginalny-7465721828036725526?refer=embed">♬ dźwięk oryginalny - ig: szybki.adder
    </a>
  </section> 
</blockquote>
