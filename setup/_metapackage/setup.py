import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-pos",
    description="Meta package for oca-pos Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-pos_access_right>=16.0dev,<16.1dev',
        'odoo-addon-pos_bypass_global_discount>=16.0dev,<16.1dev',
        'odoo-addon-pos_cash_control_override>=16.0dev,<16.1dev',
        'odoo-addon-pos_config_logo>=16.0dev,<16.1dev',
        'odoo-addon-pos_customer_comment>=16.0dev,<16.1dev',
        'odoo-addon-pos_customer_tree_view_vat>=16.0dev,<16.1dev',
        'odoo-addon-pos_daily_sales_reports_category_only>=16.0dev,<16.1dev',
        'odoo-addon-pos_default_partner>=16.0dev,<16.1dev',
        'odoo-addon-pos_discount_all>=16.0dev,<16.1dev',
        'odoo-addon-pos_edit_order_line>=16.0dev,<16.1dev',
        'odoo-addon-pos_escpos_status>=16.0dev,<16.1dev',
        'odoo-addon-pos_financial_risk>=16.0dev,<16.1dev',
        'odoo-addon-pos_global_discount_in_line>=16.0dev,<16.1dev',
        'odoo-addon-pos_hide_banknote_button>=16.0dev,<16.1dev',
        'odoo-addon-pos_lot_barcode>=16.0dev,<16.1dev',
        'odoo-addon-pos_lot_selection>=16.0dev,<16.1dev',
        'odoo-addon-pos_loyalty_exclude>=16.0dev,<16.1dev',
        'odoo-addon-pos_loyalty_redeem_payment>=16.0dev,<16.1dev',
        'odoo-addon-pos_margin>=16.0dev,<16.1dev',
        'odoo-addon-pos_membership>=16.0dev,<16.1dev',
        'odoo-addon-pos_membership_extension>=16.0dev,<16.1dev',
        'odoo-addon-pos_minimize_menu>=16.0dev,<16.1dev',
        'odoo-addon-pos_order_new_line>=16.0dev,<16.1dev',
        'odoo-addon-pos_order_remove_line>=16.0dev,<16.1dev',
        'odoo-addon-pos_order_reorder>=16.0dev,<16.1dev',
        'odoo-addon-pos_order_to_sale_order>=16.0dev,<16.1dev',
        'odoo-addon-pos_order_to_sale_order_delivery>=16.0dev,<16.1dev',
        'odoo-addon-pos_order_to_sale_order_report>=16.0dev,<16.1dev',
        'odoo-addon-pos_order_to_sale_order_sale_financial_risk>=16.0dev,<16.1dev',
        'odoo-addon-pos_partner_birthdate>=16.0dev,<16.1dev',
        'odoo-addon-pos_partner_firstname>=16.0dev,<16.1dev',
        'odoo-addon-pos_partner_location_abstract>=16.0dev,<16.1dev',
        'odoo-addon-pos_partner_location_google_map>=16.0dev,<16.1dev',
        'odoo-addon-pos_partner_sale_warning>=16.0dev,<16.1dev',
        'odoo-addon-pos_payment_change>=16.0dev,<16.1dev',
        'odoo-addon-pos_payment_description>=16.0dev,<16.1dev',
        'odoo-addon-pos_payment_method_cashdro>=16.0dev,<16.1dev',
        'odoo-addon-pos_payment_method_change_policy>=16.0dev,<16.1dev',
        'odoo-addon-pos_payment_method_image>=16.0dev,<16.1dev',
        'odoo-addon-pos_payment_restriction>=16.0dev,<16.1dev',
        'odoo-addon-pos_payment_terminal>=16.0dev,<16.1dev',
        'odoo-addon-pos_payment_usability>=16.0dev,<16.1dev',
        'odoo-addon-pos_picking_delayed>=16.0dev,<16.1dev',
        'odoo-addon-pos_price_to_weight>=16.0dev,<16.1dev',
        'odoo-addon-pos_pricelist_technical>=16.0dev,<16.1dev',
        'odoo-addon-pos_product_display_default_code>=16.0dev,<16.1dev',
        'odoo-addon-pos_product_label>=16.0dev,<16.1dev',
        'odoo-addon-pos_product_mergeable_line>=16.0dev,<16.1dev',
        'odoo-addon-pos_product_multi_barcode>=16.0dev,<16.1dev',
        'odoo-addon-pos_product_packaging_container_deposit>=16.0dev,<16.1dev',
        'odoo-addon-pos_product_packaging_multi_barcode>=16.0dev,<16.1dev',
        'odoo-addon-pos_product_quick_info>=16.0dev,<16.1dev',
        'odoo-addon-pos_receipt_hide_info>=16.0dev,<16.1dev',
        'odoo-addon-pos_receipt_hide_price>=16.0dev,<16.1dev',
        'odoo-addon-pos_receipt_replace_user_by_trigram>=16.0dev,<16.1dev',
        'odoo-addon-pos_receipt_replace_user_by_trigram_hr>=16.0dev,<16.1dev',
        'odoo-addon-pos_receipt_usability>=16.0dev,<16.1dev',
        'odoo-addon-pos_receipt_vat_detail>=16.0dev,<16.1dev',
        'odoo-addon-pos_report_session_summary>=16.0dev,<16.1dev',
        'odoo-addon-pos_reset_search>=16.0dev,<16.1dev',
        'odoo-addon-pos_sale_order_print>=16.0dev,<16.1dev',
        'odoo-addon-pos_sale_product_config_no_variant>=16.0dev,<16.1dev',
        'odoo-addon-pos_screen_element_custom_size>=16.0dev,<16.1dev',
        'odoo-addon-pos_session_pay_invoice>=16.0dev,<16.1dev',
        'odoo-addon-pos_stock_available_online>=16.0dev,<16.1dev',
        'odoo-addon-pos_supplierinfo_search>=16.0dev,<16.1dev',
        'odoo-addon-pos_ticket_extra_company_info_l10n_fr>=16.0dev,<16.1dev',
        'odoo-addon-pos_timeout>=16.0dev,<16.1dev',
        'odoo-addon-pos_to_weight_by_product_uom>=16.0dev,<16.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 16.0',
    ]
)
