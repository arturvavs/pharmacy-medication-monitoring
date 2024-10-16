sql = """SELECT     
        hcd_obter_turno_disp_atual(a.nr_seq_turno)turno,
        a.cd_setor_atendimento cd_setor_atendimento,
	    a.nr_sequencia nr_sequencia,
        p.nr_atendimento,
	    a.nr_seq_turno,
	    TO_CHAR(a.dt_prim_horario,'dd/mm hh24:mi') dt_prim_horario,
	    nvl(a.ie_reaprazado,'N') ie_reaprazado_grid,
	    substr(obter_desc_turno_disp(a.nr_seq_turno),1,255) ds_turno,
        a.nr_seq_classif,
	    substr(obter_desc_classif_lote_disp(a.nr_seq_classif),1,80) ds_classificacao,
	    replace(obter_nome_setor(a.cd_setor_atendimento),'UNIDADE DE INTERNAÇÃO ','') ds_setor_lote,
	    substr(obter_unidade_atendimento(p.nr_atendimento,'IA', 'U'),1,255) ds_leito,
        (SELECT substr(Obter_funcao_usuario_orig(x.nm_usuario_original),1,240) FROM	prescr_medica x WHERE x.nr_prescricao = a.nr_prescricao) ds_funcao_prescritor,  
        p.dt_alta_medico dt_alta_medico,
        case when exists (select 1 from ap_lote_item x, material y where x.nr_seq_lote = a.nr_sequencia and x.cd_material = y.cd_material and y.CD_MEDICAMENTO is not null) then 'ATB'
        ELSE 'SEM ATB' end ie_atb,
substr(obter_unidade_atendimento(p.nr_atendimento,'A', 'S'),1,255) ds_setor_atual
FROM	atendimento_paciente p,
	ap_lote a,
	prescr_medica m
WHERE a.nr_prescricao = m.nr_prescricao 
	AND	m.nr_atendimento = p.nr_atendimento(+) 
	AND	a.ie_status_lote = 'G' 
	AND	m.nr_atendimento is not null
	AND	a.cd_local_estoque = 70 
	AND	(obter_dados_prescricao(a.nr_prescricao,'E') = 2 OR exists (SELECT 1
FROM	ap_lote x
WHERE x.nr_lote_agrupamento = a.nr_sequencia 
	AND	obter_dados_prescricao(x.nr_prescricao,'E') = 2 )) 
	AND	((m.cd_estabelecimento is null OR m.cd_estabelecimento = 2) OR exists (SELECT 1
FROM	ap_lote x
WHERE x.nr_lote_agrupamento = a.nr_sequencia 
	AND	obter_dados_prescricao(x.nr_prescricao,'E') = 2)) 
	AND	(a.nr_lote_agrupamento is null OR a.ie_agrupamento = 'S')
   AND a.nr_seq_classif not in (13)
	AND	a.dt_prim_horario between TRUNC(SYSDATE - (6/24),'HH24')
	AND	TRUNC(SYSDATE + (6/24),'HH24')
    AND a.nr_seq_turno in (24,25,26,27)
ORDER BY 
	 a.dt_prim_horario,substr(obter_unidade_atendimento(p.nr_atendimento,'IA', 'U'),1,255)"""