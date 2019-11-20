import { LitElement, css, html } from 'lit-element'

class TranslationElement extends LitElement {
  static get styles() {
    return css`
      :host([pending]) {
        text-decoration: underline dotted
      }
    `;
  }

  render() {
    return html`<slot></slot>`
  }
}

customElements.define('grow-translation', TranslationElement);
