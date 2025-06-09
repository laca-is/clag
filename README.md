# CLAG - Controlled Natural Language for Agents

CLAG é uma linguagem natural controlada (LNC) baseada em inglês que permite especificar sistemas multiagentes de forma intuitiva e estruturada. Como uma LNC, o CLAG restringe a gramática e o vocabulário do inglês para eliminar ambiguidades e facilitar o processamento automático, mantendo a legibilidade para humanos.

## O que é uma Linguagem Natural Controlada?

Uma Linguagem Natural Controlada é um subconjunto de uma língua natural que:
- Restringe a gramática e o vocabulário
- Elimina ambiguidades
- Mantém a legibilidade para humanos
- Permite processamento automático confiável

No caso do CLAG, estas restrições são aplicadas especificamente para a especificação de agentes e seus comportamentos, utilizando o inglês como base.

## Instalação

Para instalar CLAG, você pode usar o gerenciador de pacotes `pip`:

```bash
pip install clag
```

Para atualizar sua versão já instalada do CLAG para a mais recente, você pode usar:

```bash
pip install clag -U
```

**CLAG requer `Python` 3.12+ para funcionar corretamente.**

## Como o CLAG Funciona

O CLAG utiliza uma sintaxe controlada em inglês para definir:
- Crenças dos agentes (o que eles sabem)
- Desejos dos agentes (o que eles querem alcançar)
- Planos dos agentes (como eles agem)
- Percepções do ambiente (o que os agentes podem perceber)
- Ações do ambiente (o que os agentes podem fazer)

### Estrutura Básica

```clag
Agent AgentName
  believes belief1, belief2
  desires desire1, desire2
  with plans
    plan_name when condition then action.
```

### Exemplos

#### Exemplo Básico: Hello World

```clag
Agent HelloAgent
  believes hello
  with plans
    say_hello when believes hello then achieve nothing.
```

#### Exemplo de Comunicação: Envio e Recebimento

```clag
Agent Sender
  believes is_sender
  desires to send_info
  using channel SimpleChannel
  in environment SimpleEnv
  with plans
    send_message when achieve send_info then
      send Receiver achieve hello via SimpleChannel.

Agent Receiver
  believes is_receiver
  with plans
    receive_message when achieve hello then
      achieve nothing.

Environment SimpleEnv
  that perceives message
  with actions
    receive_message.
```

#### Exemplo de Interação com Ambiente: Estacionamento

```clag
Agent Driver
  believes has_budget
  desires to park
  using channel ParkingChannel
  in environment Parking
  with plans
    ask_price when achieve park then
      send Manager achieve ask_price via ParkingChannel.
    park_car when achieve price_received then
      achieve park_car.

Agent Manager
  believes spot_price
  using channel ParkingChannel
  in environment Parking
  with plans
    send_price when achieve ask_price then
      send Driver achieve price_received via ParkingChannel.

Environment Parking
  that perceives spot_available
  with actions
    park_car.
    remove_car.
```

## Vantagens do CLAG como CNL

1. **Legibilidade**: A sintaxe é próxima do inglês natural, facilitando a compreensão
2. **Estruturação**: Regras claras de formação de frases e expressões
3. **Sem ambiguidades**: Cada construção tem um significado único e preciso
4. **Processamento automático**: Fácil conversão para código Python executável
5. **Manutenibilidade**: Código mais fácil de entender e modificar
