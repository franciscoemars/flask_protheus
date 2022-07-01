/*
Query utilizando as tabelas padrão:
SF2010 (Faturamento) e SA1010 (Clientes)

Exemplo contabilizando o faturamento dentro de período.
*/

SELECT
    TRIM(SF2.F2_CLIENTE||SF2.F2_LOJA) AS CLIENTE,
    TRIM(SA1.A1_NREDUZ) AS NOME,
    COUNT(SF2.F2_CLIENTE||SF2.F2_LOJA) AS TOTAL,
    to_char(
        SUM(SF2.F2_VALBRUT),
            'L999G999G999D99', 'nls_currency = R$ nls_numeric_Characters= ,.'
            ) FATURADO
FROM 
    SF2010 SF2
INNER JOIN 
    SA1010 SA1
        ON SF2.F2_CLIENTE||SF2.F2_LOJA = SA1.A1_COD||SA1.A1_LOJA 
            AND SA1.D_E_L_E_T_ <> '*'
WHERE
    SF2.F2_EMISSAO >= ( 
        SELECT 
            to_char(add_months(sysdate, - 1), 'yyyymmdd') 
        FROM dual
        )
GROUP BY    
    SF2.F2_CLIENTE||SF2.F2_LOJA,
    SA1.A1_NREDUZ
ORDER BY 
    TOTAL DESC






