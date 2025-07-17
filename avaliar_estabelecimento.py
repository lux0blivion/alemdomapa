def avaliar_estabelecimento(usuario, repositorio):
    print("\n=== Avaliar Estabelecimento ===")

    for i, est in enumerate(repositorio.estabelecimentos):
        media = est.media_avaliacoes() if hasattr(est, 'media_avaliacoes') else 0
        print(f"{i+1}. {est.nome} - Média: {media}")

    try:
        escolha = int(input("\nDigite o número do estabelecimento que deseja avaliar: ")) - 1
        if 0 <= escolha < len(repositorio.estabelecimentos):
            nota = int(input("Dê uma nota de 1 a 5: "))
            if nota < 1 or nota > 5:
                print("Nota inválida.")
                return
            repositorio.estabelecimentos[escolha].adicionar_avaliacao(nota)
            repositorio.salvar_tudo()
            print("✅ Avaliação registrada com sucesso!")
        else:
            print("Estabelecimento não encontrado.")
    except ValueError:
        print("Entrada inválida.")
