describe('template spec', () => {
  it('passes', () => {
    cy.visit('https://www.citilink.ru')
    cy.get('input[type="search"]').type('Монитор')
    
  })
})