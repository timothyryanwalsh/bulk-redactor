<template>
  <nav class="navbar is-primary" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <router-link class="navbar-item" to="/">
        <h4 class="title is-4" style="color: white">Bulk Reviewer</h4>
      </router-link>
      <div class="navbar-burger" @click="showNav = !showNav" :class="{ 'is-active': showNav }">
        <span></span>
        <span></span>
        <span></span>
      </div>
    </div>
    <div class="navbar-menu" :class="{ 'is-active': showNav }">
      <div class="navbar-end">
        <router-link class="navbar-item" to="/">
          <span>Sessions</span>
        </router-link>
        <router-link class="navbar-item" to="/settings">
          <span>Settings</span>
        </router-link>
        <!-- + New Session links open modal instead of routing -->
        <div class="navbar-item" v-if="!showNav">
          <a class="button is-link is-inverted is-outlined is-rounded">
            <router-link to="/" class="newSessionButton">
              + New Session
            </router-link>
          </a>
        </div>
        <a class="navbar-item" v-else>
          <router-link class="navbar-item" to="/">
          <span>+ New Session</span>
          </router-link>
        </a>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'TopNavbar',
  data () {
    return {
      showNav: false
    }
  }
}
</script>

<style>
.newSessionButton {
  color: white !important;
}
.newSessionButton:hover {
  color: #178B63 !important;
}
</style>
